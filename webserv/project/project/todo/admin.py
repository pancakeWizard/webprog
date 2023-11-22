from django.contrib import admin
from .models import TaskList, TaskCategory, TaskStatus
# Register your models here.
admin.site.register(TaskList)
admin.site.register(TaskCategory)
admin.site.register(TaskStatus)