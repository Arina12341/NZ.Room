from django.db import models
from accounts.models import User

class Event(models.Model):
    typeEvent = models.CharField(max_length=50, choices=[['exam', 'Exaxm'],['test', 'Test'],['school_events', 'School Events'],['parent-teacher_meeting','Parent-Teacher meeting'],['personal_events','Personal events']])
    title = models.TextField(max_length=25)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    duration = models.IntegerField()
    location = models.TextField()
    users = models.ManyToManyField(User)
    # task = 

    def __str__(self):
        return self.title