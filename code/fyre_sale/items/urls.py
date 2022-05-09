from django.urls import path
from . import views

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('<int:item_id>', views.item_detail, name="item_detail"),
    path('create_item', views.create_item, name="create_item")
]

