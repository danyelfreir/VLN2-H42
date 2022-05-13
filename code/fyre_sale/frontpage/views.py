from django.shortcuts import render
from items.models import ItemForSale
from users.views import calculate_average


def index(request):
    user_rating = calculate_average(request.user)
    list_of_items = ItemForSale.objects.all().order_by('date_of_upload')[:8]
    return render(request, 'frontpage/index.html', context={
        'items': list_of_items,
        'user_rating': user_rating
    })
