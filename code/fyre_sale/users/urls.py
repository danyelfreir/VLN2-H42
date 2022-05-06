from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="sign_up"),
    path('signin', views.sign_in, name="sign_in"),
    path('<str:username>', views.userpage, name="user_page")
]
