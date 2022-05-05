from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.items_index, name="items_index"),
    path('single/', views.single_item, name="single_item"),
]

