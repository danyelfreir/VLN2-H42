from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="sign_up"),
    path('signin', views.sign_in, name="sign_in")
    # path('<int:item_id>', views.singleitem.html, name="single_item")
    # path('all/', views.items_index, name="items_index"),
]