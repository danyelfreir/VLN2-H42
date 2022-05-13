from django.urls import path
from . import views

#tilraun fyrir myndauppload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('<int:item_id>', views.item_detail, name="item_detail"),
    path('create_item', views.create_item, name="create_item"),
    path('<int:item_id>/place_bid', views.place_bid, name="place_bid"),
    path('<int:offer_id>/respond/<str:response>',
         views.respond_bid,
         name="respond_bid"),
    path('offer/<int:offer_id>/accept', views.accept_bid, name="accept_bid"),
    path('offer/<int:offer_id>/decline', views.decline_bid,
         name="decline_bid"),
    path('<int:item_id>/edit_ad', views.edit_ad, name="edit_ad"),
    path('api/search', views.item_search, name="item_search"),
    path('api/get_images/<int:item_id>', views.get_images, name="get_images"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
