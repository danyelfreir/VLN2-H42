from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
<<<<<<< HEAD
    path('profile/<str:username>', views.profilepage, name="profile"),
=======
    #path('<str:username>', views.userpage, name="user_page"),
    path('profile', views.profilepage, name="profile"),
>>>>>>> 3ac6c3b0b5e0f0ec19845c85cb11514789467308
    path('profile/inbox/', views.inbox, name="inbox"),
    path('profile/inbox/<str:params>', views.inbox, name="inbox"),
    path('profile/inbox/notifications/<int:not_id>', views.notifications, name="notifications"),
    path('payment', views.payment, name="payment"),
    path('address', views.address, name="address")
]
