
from django.urls import path, include
from .views import SignUp, terms_conditions, UserPasswordChangeView, subscribe, thank_you

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("signup/", SignUp.as_view(), name="signup"),
    path("terms_conditions/", terms_conditions, name="terms_conditions"),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('subscribe/', subscribe, name='subscribe'),
    path('thank_you/', thank_you, name='thank_you'),

]
