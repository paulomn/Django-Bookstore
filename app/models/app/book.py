from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=8)

    def __str__(self):
        return self.title + '-' + self.author
