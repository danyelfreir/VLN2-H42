from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from items.models import ItemForSale
from users.models import Notification
from items.models import ItemForSale, SubCategory, Category, Offer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from items.item_form import CreateItem, PlaceBid, EditAd
import datetime



def items_index(request):
    name, subcat, cat = check_query(request)
    list_of_items, categories, subcategories = None, None, None

    if name is None and subcat is None and cat is None:
        list_of_items = ItemForSale.objects.all().order_by('date_of_upload')
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

# def exclude_item(items, detailed_item):
#
#     for item in items:
#         if item.id == detailed_item.id:
#             items = items.exclude(id=item.id)
#         else:
#             continue
#     return items

def item_detail(request, item_id):
    detailed_item = ItemForSale.objects.get(pk=item_id)
    seller_user = User.objects.get(pk=detailed_item.seller_id)
    similar_items = ItemForSale.objects.filter(sub_cat=detailed_item.sub_cat_id)
    similar_items_cleaned = similar_items.exclude(id=detailed_item.id)
    return render(request, 'items/singleitem.html', context={
        'item': detailed_item,
        'seller': seller_user,
        'similar_items': similar_items_cleaned
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


@login_required
def create_item(request):
    date = datetime.datetime.now()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = CreateItem(request.POST, request.FILES)
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


@login_required
def place_bid(request, item_id):
    chosen_item = ItemForSale.objects.get(pk=item_id)
    if chosen_item.seller == request.user:
        raise Http404()
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


@login_required
def respond_bid(request, offer_id, response):
    offer = Offer.objects.get(pk=offer_id)
    return render(request, 'items/respond_bid.html', context={
        'response': response,
        'offer': offer,
    })


@login_required
def accept_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    offer_obj.approved = True
    offer_obj.save()
    date_time = datetime.datetime.now()
    notify(offer_obj, offer_obj.buyer, date_time)
    return redirect('inbox', username=request.user.username)


@login_required
def decline_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    date_time = datetime.datetime.now()
    notify(offer_obj, offer_obj.buyer, date_time)
    return redirect('inbox', username=request.user.username)


@login_required
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


def notify(offer_obj, recipient, date_time):
    new_not = Notification.objects.create(
        recipient=recipient,
        offer=offer_obj,
        timestamp=date_time
    )

@login_required
def edit_ad(request, item_id):
    chosen_item = ItemForSale.objects.get(pk=item_id)
    if chosen_item.seller == request.user:
        raise Http404()
    instance = get_object_or_404(ItemForSale, pk=item_id)
    if request.method == 'POST':
        date = datetime.datetime.now()
        form = EditAd(chosen_item, request.POST, instance=instance)
        if form.is_valid():
            item_obj = form.save(commit=False)
            item_obj.min_bid = chosen_item.cur_bid
            item_obj.seller_id = chosen_item.seller_id
            item_obj.date_of_upload = date
            item_obj.save()
            return redirect('items_index')
        else:
            print(form.errors)
    else:
        form = EditAd()
    return render(request, 'items/editad.html', {
        'form': form,
        'item': chosen_item,

    })
