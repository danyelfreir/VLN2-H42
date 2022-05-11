from django.shortcuts import render, redirect
from django.http import JsonResponse
from items.models import ItemForSale
from users.models import Notification
from items.models import ItemForSale, SubCategory, Category, Offer
from django.contrib.auth.models import User
from items.item_form import CreateItem, PlaceBid
import datetime



def items_index(request):
    name, subcat, cat = check_query(request)
    list_of_items, categories, subcategories = None, None, None

    if name is None and subcat is None and cat is None:
        list_of_items = ItemForSale.objects.all().order_by('time_of_upload')
    elif name is not None and subcat is None and cat is None:
        list_of_items = ItemForSale.objects.filter(name__icontains=name)
        subcategories = None
    elif name is None and subcat is None and cat is not None:
        list_of_items = ItemForSale.objects.raw(
            ''' SELECT * FROM items_itemforsale I WHERE I.sub_cat_id in (
                    SELECT S.id FROM items_subcategory S WHERE S.category_id = (
                        SELECT C.id FROM items_category C WHERE C.name = %s))
                ORDER BY i.time_of_upload DESC; ''', [cat]
        )
        tmp_cat = Category.objects.get(name=cat)
        subcategories = SubCategory.objects.filter(category_id=tmp_cat)
    categories = Category.objects.all().order_by('name')
    return render(request, 'items/itempage.html', context={
        'items': list_of_items,
        'categories': categories,
        'subcategories': subcategories
    })


def item_detail(request, item_id):
    detailed_item = ItemForSale.objects.get(pk=item_id)
    seller_user = User.objects.get(pk=detailed_item.seller_id)
    return render(request, 'items/singleitem.html', context={
        'item': detailed_item,
        'seller': seller_user
    })


def item_search(request):
    # subcategory = SubCategory.objects.get(name=request.GET['subcat'])
    # if subcategory == 'All':
    #     results = ItemForSale.objects.filter(name__icontains=request.GET['name'])
    # else:
    #     results = ItemForSale.objects.filter(sub_cat_id=subcategory.id, name__icontains=request.GET['name'])
    results = ItemForSale.objects.filter(name__icontains=request.GET['name'])
    data = list(results.values())
    return JsonResponse({
        'results': data,
    })


def create_item(request):
    date = datetime.datetime.now()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = CreateItem(request.POST)
        if form.is_valid():
            item_obj = form.save(commit=False)
            item_obj.seller_id = tmp_user.id
            item_obj.date_of_upload = date.strftime("%x")
            item_obj.time_of_upload = date.strftime("%X")
            item_obj.cur_bid = item_obj.min_bid
            item_obj.save()
            return redirect('items_index')
    form = CreateItem()
    return render(request, 'items/create_item.html', {
        'form': form
    })

def place_bid(request, item_id):
    chosen_item = ItemForSale.objects.get(pk=item_id)
    if request.method == 'POST':
        date = datetime.datetime.now()
        bidding_user = User.objects.get(username=request.user)
        form = PlaceBid(chosen_item, request.POST)
        if form.is_valid():
            offer_obj = form.save(commit=False)
            offer_obj.buyer = bidding_user
            offer_obj.time_of_offer = date
            offer_obj.item = chosen_item
            offer_obj.save()
            chosen_item.cur_bid = offer_obj.price
            chosen_item.save()
            notify(offer_obj, chosen_item.seller, date)
            return redirect('items_index')
        else:
            print(form.errors)
    else:
        form = PlaceBid()
    return render(request, 'items/placebid.html', {
        'form': form,
        'item': chosen_item,
    })

def respond_bid(request, offer_id, response):
    offer = Offer.objects.get(pk=offer_id)
    return render(request, 'items/respond_bid.html', context={
        'response': response,
        'offer': offer,
    })

def accept_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    offer_obj.approved = True
    offer_obj.save()
    date_time = datetime.datetime.now()
    notify(offer_obj, offer_obj.buyer, date_time)
    return redirect('inbox')

def decline_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    date_time = datetime.datetime.now()
    notify(offer_obj, offer_obj.buyer, date_time)
    return redirect('inbox')

def checkout(request, offer_id):
    pass


# ======= HELPER FUNCTIONS =========

def check_query(req):
    try:
        name = req.GET['name']
    except KeyError:
        name = None
    try:
        subcat = req.GET['subcat']
    except KeyError:
        subcat = None
    try:
        cat = req.GET['cat']
    except KeyError:
        cat = None
    return name, subcat, cat

# def update_cur_bid_and_notify(item_obj, offer_obj, date_time):
#     x = Notification.objects.create(
#         recipient=item_obj.seller,
#         offer=offer_obj,
#         timestamp=date_time
#     )

def notify(offer_obj, recipient, date_time):
    new_not = Notification.objects.create(
        recipient=recipient,
        offer=offer_obj,
        timestamp=date_time
    )
