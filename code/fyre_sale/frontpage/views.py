from django.shortcuts import render
from items.models import ItemForSale


def index(request):
    list_of_items = ItemForSale.objects.all().order_by('date_of_upload')[:8]
    return render(request, 'frontpage/index.html', context={
        'items': list_of_items,
    })
