from datetime import datetime

from django.http import HttpResponse
from .models import Event
from django.shortcuts import render, redirect
from .forms import EventForm, CommentForm
def events_list(request):
    events=Event.objects.all()
    if request.GET.get('search'):
        events=events.filter(title__icontains=request.GET.get('search'))
    if request.GET.get('mode'):
        if request.GET.get('mode') == 'past':
            events=events.filter(start_date__lt=datetime.now())
        if request.GET.get('mode') == 'future':
            events=events.filter(start_date__gt=datetime.now())
    return render(
        request, 'events/events_calendar.html',
        {'events': events}
    )
def event_detail(request, pk):
    form = CommentForm
    event=Event.objects.get(id=pk)
    return render(
        request, 'events/event_detail.html',
        {'event': event, 'form': form}
    )
def event_form(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/list/')
    else:          
        form=EventForm()
    return render(
        request, 'events/event_form.html',
        {'form': form}
    )
def save_comment_form(request):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
    return HttpResponse("OK")
