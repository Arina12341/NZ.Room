from .models import Event
from django.shortcuts import render, redirect
from .forms import EventForm
def events_list(request):
    events=Event.objects.all()
    return render(
        request, 'events/events_calendar.html',
        {'events': events}
    )
def event_detail(request, pk):
    event=Event.objects.get(id=pk)
    return render(
        request, 'events/event_detail.html',
        {'event': event}
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
