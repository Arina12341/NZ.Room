from tasks.forms import TaskForm
from .models import Task
from django.shortcuts import redirect, render
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

def task_form(request):
    if request.method=='POST':
            form=TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/tasks/list/')
    else:          
        form=TaskForm()
    return render(
        request, 'tasks/task_form.html',
        {'form': form}
    )
