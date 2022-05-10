from django.shortcuts import render, redirect
from django.http import JsonResponse
from items.models import *
from django.contrib.auth.models import User
from items.item_form import CreateItem
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


def create_item(request):
    date = datetime.datetime.now()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = CreateItem(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.seller_id = tmp_user.id
            x.date_of_upload = date.strftime("%x")
            x.time_of_upload = date.strftime("%X")
            x.save()
            return redirect('items_index')
    form = CreateItem()
    return render(request, 'items/create_item.html', {
        'form': form
    })
