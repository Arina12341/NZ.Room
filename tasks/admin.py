from django.contrib import admin
from tasks.models import Task 

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
