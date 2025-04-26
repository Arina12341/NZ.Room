
from django.db import models
class Task(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    end_date=models.DateField()
    
    def _str_(self):
        return self.title 



