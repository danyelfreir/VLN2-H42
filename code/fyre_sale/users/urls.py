from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    path('<str:username>', views.profilepage, name="profile"),
    path('<str:username>/inbox/', views.inbox, name="inbox"),
    path('<str:username>/inbox/notification/<int:not_id>', views.notification, name="notification"),
    path('<str:username>/payment', views.payment, name="payment"),
    path('<str:username>/address', views.address, name="address")
]
