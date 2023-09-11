from django.contrib import admin
from django.apps import AppConfig
from .models import  UserProfile, Subscription


class AccountsConfig(AppConfig):
    name = 'accounts'

admin.site.register(UserProfile)
admin.site.register(Subscription)