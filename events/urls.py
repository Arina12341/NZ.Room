from django.urls import path

from events.views import events_list, event_detail
urlpatterns = [
    path('list/', events_list),
    path('detail/<int:pk>/', event_detail)
]