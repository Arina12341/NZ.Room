from django.contrib import admin

from accounts.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_display_links = ['username']
    