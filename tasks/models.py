
from django.db import models


class TASK_STATUS:
    NEW='new'
    IN_PROGRESS='in_progress'
    NOT_DONE='not_done'
    DONE='done'
    CHOICES=[
        (NEW,'New')
        (IN_PROGRESS,'In progress')
        (NOT_DONE,'Not done')
        (DONE,'Done')
    ]


class Task(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    end_date=models.DateField()
    status=models.CharField(max_length=50,choices=TASK_STATUS.CHOICES,default=TASK_STATUS.NEW)

    def __str__(self):
        return self.title 


