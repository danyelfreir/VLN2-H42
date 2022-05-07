from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('<int:item_id>', views.item_detail, name="item_detail")
]
