
from django import forms
from django.utils import timezone
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
    
    def clean_start_date(self):
        dt = self.cleaned_data['start_date']
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt
    def clean_end_date(self):
        dt = self.cleaned_data['end_date']
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comentar
        fields=[
            "text",
            "user",
            "event",
        ]