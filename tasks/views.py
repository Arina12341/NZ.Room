from .models import Task
from django.shortcuts import render
def tasks_list(request):
    tasks=Task.objects.all()
    return render(
        request, 'tasks/tasks_list.html',
        {'tasks': tasks}
    )
