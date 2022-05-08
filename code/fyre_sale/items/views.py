from django.shortcuts import render
from django.http import JsonResponse
from items.models import *
from users.models import User


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


# def items_index(request):
#     try:
#         tmp_cat_id = Category.objects.get(name=request.GET['cat'])
#         subcategories = SubCategory.objects.filter(category=tmp_cat_id)
#         list_of_items = ItemForSale.objects.raw(
#             ''' SELECT * FROM items_itemforsale I WHERE I.sub_cat_id in (
#                     SELECT S.id FROM items_subcategory S WHERE S.category_id = (
#                         SELECT C.id FROM items_category C WHERE C.name = %s))
#                 ORDER BY i.time_of_upload DESC; ''', [request.GET['cat']]
#         )
#     except KeyError:
#         subcategories = SubCategory.objects.all().order_by('name')
#         list_of_items = ItemForSale.objects.all().order_by('time_of_upload')
#
#     try:
#         tmp_subcat_id = SubCategory.objects.get(name=request.GET['subcat'])
#         list_of_items = ItemForSale.objects.filter(sub_cat_id=tmp_subcat_id).order_by('time_of_upload')
#     except KeyError:
#         print("Subcategory query does not exist")
#     all_categories = Category.objects.all().order_by('name')
#
#     return render(request, 'items/itempage.html', context={
#         'items': list_of_items,
#         'categories': all_categories,
#         'subcategories': subcategories
#     })


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
