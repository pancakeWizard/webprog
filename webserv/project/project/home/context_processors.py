from todo.models import TaskList
from django.contrib.auth.models import User

def task_amount(request):
    user = request.user
    task_amount = 0
    if user.is_authenticated:
        taskList = TaskList.objects.all()
        username_auth = user.username
        for task in taskList:
            if task.username == username_auth and task.status == 1:
                task_amount += 1
    return ({'task_amount':task_amount})