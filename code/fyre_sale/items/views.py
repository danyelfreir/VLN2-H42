from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404
from items.models import ItemForSale, SoldItem
from users.views import notify
from users.models import Notification
# from django.core.mail import send_mail
from items.models import ItemForSale, SubCategory, Category, Offer, ItemImages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.views import notify

from items.item_form import CreateItem, PlaceBid, GetImages, EditAd
from datetime import datetime
from enum import Enum


class FilterSort(Enum):
    PRICE_ASC = 0
    PRICE_DESC = 1
    DATE_ASC = 2
    DATE_DESC = 3


def items_index(request):
    name, subcat, cat = check_query(request)
    list_of_items, categories, subcategories = None, None, None
    title = None

    if name is None and subcat is None and cat is None:
        list_of_items = ItemForSale.objects.filter(
            sold=False).order_by('date_of_upload')
    elif name is not None and subcat is None and cat is None:
        list_of_items = ItemForSale.objects.filter(name__icontains=name,
                                                   sold=False)
        subcategories = None
    elif name is None and subcat is None and cat is not None:
        tmp_cat = Category.objects.get(name=cat)
        tmp_subcat = SubCategory.objects.all()
        subcategories = tmp_subcat.filter(category=tmp_cat)
        list_of_items = ItemForSale.objects.filter(sold=False)
        for sc in tmp_subcat:
            if sc.category == tmp_cat:
                continue
            list_of_items = list_of_items.exclude(sub_cat=sc)
        title = cat
    elif name is None and subcat is not None and cat is not None:
        tmp_cat = Category.objects.get(name=cat)
        tmp_scat = SubCategory.objects.get(name=subcat)
        subcategories = SubCategory.objects.filter(category=tmp_cat)
        list_of_items = ItemForSale.objects.filter(sub_cat=tmp_scat,
                                                   sold=False)
        title = f'{cat} - {subcat}'
    categories = Category.objects.all().order_by('name')
    return render(request,
                  'items/itempage.html',
                  context={
                      'items': list_of_items,
                      'categories': categories,
                      'subcategories': subcategories,
                      'title': title,
                  })


def item_detail(request, item_id):
    detailed_item = get_object_or_404(ItemForSale, pk=item_id)
    seller_user = User.objects.get(pk=detailed_item.seller_id)
    similar_items = ItemForSale.objects.filter(
        sub_cat=detailed_item.sub_cat_id)
    similar_items_cleaned = similar_items.exclude(id=detailed_item.id)
    return render(request,
                  'items/singleitem.html',
                  context={
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


def get_images(request, item_id):
    results = ItemImages.objects.filter(item_id=item_id)
    data = list(results.values())
    print(data)
    return JsonResponse({
        'results': data,
    })


@login_required
def create_item(request):
    date = datetime.now()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = CreateItem(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            item_obj = form.save(commit=False)
            item_obj.seller_id = tmp_user.id
            item_obj.date_of_upload = date.strftime("%x")
            item_obj.cur_bid = item_obj.min_bid
            item_obj.save()

            count = 1
            for image in images:
                if count > 1:
                    photo = ItemImages.objects.create(
                        item=item_obj,
                        image=image,
                        main_image=True,
                    )
                else:
                    photo = ItemImages.objects.create(
                        item=item_obj,
                        image=image,
                        main_image=False,
                    )

            return redirect('items_index')
    form = CreateItem()
    images = GetImages()
    return render(request, 'items/create_item.html', {
        'form': form,
        'images': images
    })


@login_required
def place_bid(request, item_id):
    chosen_item = ItemForSale.objects.get(pk=item_id)
    if chosen_item.seller == request.user:
        raise Http404()
    if request.method == 'POST':
        date = datetime.now()
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

            notif_content = f'"place_bid"  {request.user.username} placed a bid on {chosen_item.name}'
            notify(offer_obj, chosen_item.seller, notif_content, date)
            return redirect('items_index')
    else:
        form = PlaceBid()
    return render(request, 'items/placebid.html', {
        'form': form,
        'item': chosen_item,
    })


@login_required
def respond_bid(request, offer_id, response):
    offer = Offer.objects.get(pk=offer_id)
    return render(request,
                  'items/respond_bid.html',
                  context={
                      'response': response,
                      'offer': offer,
                  })


@login_required
def accept_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    offer_obj.approved = True
    offer_obj.save()
    date_time = datetime.now()

    item_obj = ItemForSale.objects.get(pk=offer_obj.item_id)
    item_obj.sold = True
    item_obj.save()

    SoldItem.objects.create(offer=offer_obj, item=item_obj)

    notif_content = f'"accept_bid" {request.user.username} has accepted your offer on {offer_obj.item.name}'
    notify(offer_obj, offer_obj.buyer, notif_content, date_time)
    return redirect('inbox', username=request.user.username)


@login_required
def decline_bid(request, offer_id):
    offer_obj = Offer.objects.get(pk=offer_id)
    date_time = datetime.now()

    notif_content = f'"decline_bid"{request.user.username} has rejected your offer on {offer_obj.item.name}'
    notify(offer_obj, offer_obj.buyer, notif_content, date_time)
    return redirect('inbox', username=request.user.username)


@login_required
def edit_ad(request, item_id):
    chosen_item = ItemForSale.objects.get(pk=item_id)
    if chosen_item.seller != request.user:
        raise Http404()
    instance = get_object_or_404(ItemForSale, pk=item_id)
    if request.method == 'POST':
        date = datetime.now()
        form = EditAd(chosen_item, request.POST, instance=instance)
        if form.is_valid():
            item_obj = form.save(commit=False)
            item_obj.min_bid = chosen_item.cur_bid
            item_obj.seller_id = chosen_item.seller_id
            item_obj.date_of_upload = date
            item_obj.save()
            return redirect('items_index')
    else:
        form = EditAd(instance=instance)
    return render(request, 'items/editad.html', {
        'form': form,
        'item': chosen_item,
    })


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
