from django.db import models
from django.contrib.auth.models import AbstractUser
USER_TYPE_CHOICES = (
    ("worker","mardikor"),
    ("employer","ish beruvchi"),
)
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    rating = models.FloatField(default=0)
    user_type = models.CharField(max_length=10,choices=USER_TYPE_CHOICES)
    address=models.CharField(max_length=255, blank=True)
    bio=models.TextField(blank=True)
    def __str__(self):
        return f"{self.username} - {self.user_type}"

