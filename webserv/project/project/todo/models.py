from django.db import models

# Create your models here.
class TaskList(models.Model):
    username     = models.TextField        ('user')
    task         = models.TextField        ('task')
    status       = models.IntegerField     ('status')
    category     = models.IntegerField     ('category')

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

class TaskCategory(models.Model):
    category_name = models.TextField ('category_name')

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class TaskStatus(models.Model):
    status_name = models.TextField ('status_name')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'