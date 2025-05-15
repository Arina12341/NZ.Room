
from django import forms

from events.models import Event, Comentar


class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=[
            "typeEvent",
            "title",
            "content",
            "start_date",
            "end_date",
            "users",
            "task",
        ]
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comentar
        fields=[
            "text",
            "user",
            "event",
        ]