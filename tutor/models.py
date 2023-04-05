from django.db import models


# Create your models here.

class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    question = models.TextField()
    answer = models.TextField()

