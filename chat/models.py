from django.contrib.auth.models import User
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(User)
    created= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    is_read = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

