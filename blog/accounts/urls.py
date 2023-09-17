
from django.urls import path, include
from .views import SignUp, terms_conditions, UserAccount,  UserPasswordChangeView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name="signup"),
    path("terms_conditions/", terms_conditions, name="terms_conditions"),
    path('password-change/', UserPasswordChangeView.as_view(),
         name='password_change'),
    path("user_account/", UserAccount.as_view(), name="user_account"),

]
