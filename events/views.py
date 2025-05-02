from .models import Event
from django.shortcuts import render
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