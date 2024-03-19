from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    book_id = models.CharField(max_length=10)

    def __str__(self):
        return self.title