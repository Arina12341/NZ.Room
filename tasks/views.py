from .models import Task
from django.shortcuts import render
def tasks_list(request):
    tasks=Task.objects.all()
    return render(
        request, 'tasks/tasks_list.html',
        {'tasks': tasks}
    )

def task_detail(request, pk):
    task=Task.objects.get(id=pk)
    return render(
        request, 'tasks/task_detail.html',
        {'task': task}
    )