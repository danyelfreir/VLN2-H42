from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from . import views

urlpatterns = [
    path('signup', views.sign_up, name="signup"),
    path('signin', views.sign_in, name="signin"),
    path('signout', LogoutView.as_view(next_page="signin"), name="signout"),
    path('<str:username>', views.profilepage, name="profile"),
    path('<str:username>/rate/<int:not_id>', views.rate_sales, name="rate_sales"),
    path('<str:username>/inbox/', views.inbox, name="inbox"),
    path('<str:username>/inbox/notification/<int:not_id>', views.notification, name="notification"),
    path('<str:username>/inbox/notification/<int:not_id>/rate_sales', views.rate_sales, name="rate_sales"),
    path('<str:username>/edit/payment', views.edit_payment, name="edit_payment"),
    path('<str:username>/edit/address', views.edit_address, name="edit_address"),
    path('<str:username>/edit/profile', views.edit_profile, name="edit_profile"),
    path('checkout/<int:not_id>/<int:step>', views.checkout, name="checkout"),
    path('checkout/<int:not_id>/confirm', views.checkout_confirm, name="checkout_confirm"),
    path('checkout/clean', views.clean_checkout_session, name="clean"),
    path('api/get_rating/<int:user_id>', views.get_rating, name="get_rating"),
]
