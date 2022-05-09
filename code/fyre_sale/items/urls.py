from django.template.defaulttags import url
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.items_index, name="items_index"),
    path('<int:item_id>', views.item_detail, name="item_detail"),
    path('search/', views.item_search, name='item_search'),
]
