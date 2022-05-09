from django.shortcuts import render
from items.models import ItemForSale, SubCategory
from users.models import User


def index(request):
    list_of_items = ItemForSale.objects.all().order_by('time_of_upload')[:8]
    subcategories = SubCategory.objects.all().order_by('name')
    # user_info = User.objects.
    return render(request, 'frontpage/index.html', context={
        'items': list_of_items,
        'subcategories': subcategories,
    })
