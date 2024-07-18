from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200 , blank=True)
    auther = models.CharField(max_length=200)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.title
