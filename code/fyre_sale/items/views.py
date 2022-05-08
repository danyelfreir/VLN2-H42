from django.shortcuts import render
from django.http import HttpResponse
from items.models import *
from users.models import User

# Create your views here.
def items_index(request):
    list_of_items = ItemForSale.objects.all().order_by('time_of_upload')
    all_categories = Category.objects.all().order_by('name')
    all_subcategories = SubCategory.objects.all()
    return render(request, 'items/itempage.html', context={
        'items': list_of_items,
        'categories': all_categories,
        'subcategories': all_subcategories
    })

def item_detail(request, item_id):
    detailed_item = ItemForSale.objects.get(pk=item_id)
    seller_user = User.objects.get(pk=detailed_item.seller_id)
    return render(request, 'items/singleitem.html', context={
        'item': detailed_item,
        'seller': seller_user
    })

def create_item(request):
    if request.method == 'POST':
        print('test1')
    else:
        print('test2')