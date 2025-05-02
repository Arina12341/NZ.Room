from django.urls import path

from events.views import events_list
urlpatterns = [
    path('list/', events_list)
]