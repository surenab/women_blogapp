from django.contrib import admin

from .models import Blog, Message, BlogComment, AboutTeam, TeamMember


class MessageAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject", "created_on"]


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ["full_name", "job_position"]


admin.site.register(Blog)
admin.site.register(Message, MessageAdmin)
admin.site.register(AboutTeam)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(BlogComment)
