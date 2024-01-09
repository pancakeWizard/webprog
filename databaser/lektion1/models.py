from django.db import models

# Create your models here.
class Celebrity(models.Model):
    name = models.CharField(max_length=25)
    age  = models.IntegerField()

    class Meta:
        verbose_name = 'Celebrity'
        verbose_name_plural = 'Celebrities'