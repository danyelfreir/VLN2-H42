from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    path('profile/<str:username>', views.profilepage, name="profile"),
    path('profile/inbox/', views.inbox, name="inbox"),
    path('profile/inbox/<str:params>', views.inbox, name="inbox"),
    path('profile/inbox/notifications/<int:not_id>', views.notification, name="notification"),
    path('payment', views.payment, name="payment"),
    path('address', views.address, name="address"),
    path('edit_user', views.edit_user, name="edit_user"),
]
