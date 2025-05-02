from django.db import models
from accounts.models import User
from tasks.models import Task


class EVENT_TYPES:
    EXAM = 'exam'
    TEST = 'test'
    SCHOOL_EVENTS = 'school_events'
    PARENT_TEACHER_MEETING = 'parent_teacher_meeting'
    PERSONAL_EVENTS = 'personal_events'

    choices=[
        [EXAM, 'Exam'],
        [TEST, 'Test'],
        [SCHOOL_EVENTS, 'School Events'],
        [PARENT_TEACHER_MEETING,'Parent-Teacher meeting'],
        [PERSONAL_EVENTS,'Personal events']
    ]


class Event(models.Model):
    typeEvent = models.CharField(max_length=25, choices=EVENT_TYPES.choices, default=EVENT_TYPES.SCHOOL_EVENTS)
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, default=15)
    location = models.TextField(blank=True, default='')
    users = models.ManyToManyField(User)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title