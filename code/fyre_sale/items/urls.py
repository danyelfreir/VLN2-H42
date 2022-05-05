from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('item/<int:item_id>', views.single_item, name="single_item")
    # path('all/', views.items_index, name="items_index"),
]

