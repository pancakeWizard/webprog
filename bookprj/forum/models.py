from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    author = models.ManyToManyField(Author, blank=True)
    likes = models.PositiveIntegerField(null=True, default=0)
    dislikes = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return self.title

class Recension(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET('Okänd användare'))
    time = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(null=True, default=0)
    dislikes = models.PositiveIntegerField(null=True, default=0)

    def __str__(self):
        return f'{self.author} - {self.book}'