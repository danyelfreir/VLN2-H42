from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('<int:item_id>', views.item_detail, name="item_detail"),
    path('create_item', views.create_item, name="create_item"),
    path('search', views.item_search, name="item_search"),
    path('<int:item_id>/place_bid', views.place_bid, name="place_bid"),
    path('<int:offer_id>/respond/<str:response>', views.respond_bid, name="respond_bid"),
    path('offer/<int:offer_id>/accept', views.accept_bid, name="accept_bid"),
    path('offer/<int:offer_id>/decline', views.decline_bid, name="decline_bid"),
    path('offer/<int:offer_id>/checkout', views.checkout, name="checkout")
]
