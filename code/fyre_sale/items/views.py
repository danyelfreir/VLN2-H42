from django.shortcuts import render
from django.http import HttpResponse
from items.models import ItemForSale

# Create your views here.
def items_index(request):
    return render(request, 'items/itempage.html', context={
        'items': ItemForSale.objects.all().order_by('time_of_upload')
})

def single_item(request, item_id):
    return HttpResponse("Detail on item", item_id)
    #return reverse(request, 'items/test.html')
