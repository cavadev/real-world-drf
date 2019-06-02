from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email
