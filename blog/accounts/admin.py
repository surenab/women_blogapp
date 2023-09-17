from django.contrib import admin
from django.apps import AppConfig
from .models import UserProfile


class AccountsConfig(AppConfig):
    name = 'accounts'


admin.site.register(UserProfile)

