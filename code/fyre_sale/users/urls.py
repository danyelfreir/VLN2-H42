from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views
#fyrir checkout
# from . import Checkout
# from .forms import AddressInsert, PaymentInsert



urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    path('<str:username>', views.profilepage, name="profile"),
    path('<str:username>/inbox/', views.inbox, name="inbox"),
    path('<str:username>/inbox/notification/<int:not_id>', views.notification, name="notification"),
    path('<str:username>/edit/payment', views.edit_payment, name="edit_payment"),
    path('<str:username>/edit/address', views.edit_address, name="edit_address"),
    path('<str:username>/edit/profile', views.edit_profile, name="edit_profile"),
    path('checkout/<int:offer_id>/<int:step>', views.checkout, name="checkout"),
    path('checkout/clean', views.clean_checkout_session, name="clean")
]
