from django.urls import path

from tasks.views import tasks_list
urlpatterns = [
    path('list/', tasks_list)
]