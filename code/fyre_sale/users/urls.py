from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    # path('signin', LoginView.as_view(template_name="users/signin.html"), name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    #path('<str:username>', views.userpage, name="user_page"),
    path('profile', views.profilepage, name="profile"),
    path('profile/inbox/', views.inbox, name="inbox"),
    path('profile/inbox/<str:params>', views.inbox, name="inbox"),
    path('profile/inbox/notifications/<int:not_id>', views.notifications, name="notifications"),
    path('payment', views.payment, name="payment"),
    path('address', views.address, name="address")
]
