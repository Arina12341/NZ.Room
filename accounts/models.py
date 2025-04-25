from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    #name=models.CharField(max_length=100)
    role=models.CharField(
        max_length=10, 
        choices=[["teacher","Teacher"],["student","Student"],["perent","Parent"]]
    )
