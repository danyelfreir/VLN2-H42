from django.shortcuts import render, redirect
from items.models import *
from django.contrib.auth.models import User
from items.item_form import CreateItem
import datetime

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
    date = datetime.datetime.now()
    if request.method == 'POST':
        tmp_user = User.objects.get(username=request.user)
        form = CreateItem(data=request.POST)

        print(form.fields)
        if form.is_valid():
            print("Valid")
            form.fields['seller'].value = tmp_user.id
            form.fields['date_of_upload'].value = date.strftime("%x")
            form.fields['time_of_upload'].value = date.strftime("%X")
            form.save()
            return redirect('item_index')
    form = CreateItem()
    return render(request, 'items/create_item.html', {
        'form': form
    })