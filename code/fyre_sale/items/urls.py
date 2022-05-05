from django.urls import include, path
from . import views

urlpatterns = [
    path('all/', views.items_index, name="items_index"),
]
