from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200),
    summary = models.CharField(max_length=150),
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title

