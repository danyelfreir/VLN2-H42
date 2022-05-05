from django.shortcuts import render
from items.models import ItemForSale

# Create your views here.
def items_index(request):
    return render(request, 'items/itempage.html', context={
        'items': ItemForSale.objects.all().order_by('time_of_upload')
})
