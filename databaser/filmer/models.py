from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=25)
    age  = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=250)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    year = models.IntegerField()
    length = models.IntegerField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title