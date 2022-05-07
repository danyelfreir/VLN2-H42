from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="sign_up"),
    # path('signin', views.sign_in, name="sign_in"),
    path('signin', LoginView.as_view(template_name="users/signin.html"), name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    path('<str:username>', views.userpage, name="user_page")
]
