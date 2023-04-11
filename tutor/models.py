from django.db import models


# Create your models here.

class Message(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    question = models.TextField()
    answer = models.TextField()


class Page(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    page_source = models.TextField()
    page_number = models.CharField(max_length=10)
    page_content = models.TextField()
