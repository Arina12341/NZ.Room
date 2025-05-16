from datetime import datetime

from django.http import HttpResponse
from .models import Comentar, Event
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
    event=Event.objects.get(id=pk)
    comments = Comentar.objects.filter(event=event).order_by('-create_date')
    return render(
        request, 'events/event_detail.html',
        {'event': event, 'comments': comments}
    )
def event_form(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events/list/')
        print(form.errors)
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
            return redirect('/events/detail/'+ request.POST.get('event') +'/')
    return redirect('/events/list/')
