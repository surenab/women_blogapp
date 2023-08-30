from django.contrib import admin
from .models import Blog, Message, BlogComment

class Messagedmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject", "created_on"]


admin.site.register(Blog)
admin.site.register(Message, Messagedmin)
admin.site.register(BlogComment)

