from django.urls import path

from events.views import events_list, event_detail, event_form, save_comment_form
urlpatterns = [
    path('list/', events_list),
    path('detail/<int:pk>/', event_detail),
    path('create/', event_form),
    path('save_comment/', save_comment_form)
]