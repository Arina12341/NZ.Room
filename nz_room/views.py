
from django.http import HttpResponse
from django.shortcuts import render
from events.models import Event
from tasks.models import Task

def home(request):
    events=Event.objects.all()[:6]
    tasks=Task.objects.all()[:6]
    return render(request, 'home.html', context={"events": events, "tasks": tasks})
