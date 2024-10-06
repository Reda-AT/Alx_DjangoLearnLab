from django.db import models

# Create your models here.

class Book(models.Model):
    models.CharField, "max_length", 200, "title" , "author"
    author = models.CharField , 100,
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title