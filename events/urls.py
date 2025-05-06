from django.urls import path

from events.views import events_list, event_detail, event_form
urlpatterns = [
    path('list/', events_list),
    path('detail/<int:pk>/', event_detail),
    path('create/', event_form),
]