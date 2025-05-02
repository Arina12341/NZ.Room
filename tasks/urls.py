from django.urls import path

from tasks.views import tasks_list, task_detail
urlpatterns = [
    path('list/', tasks_list),
    path('detail/<int:pk>/', task_detail)
]