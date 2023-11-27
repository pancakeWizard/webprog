from django.shortcuts import render
from . models import TaskList, TaskCategory, TaskStatus
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse 

# Create your views here.
def toDo(request):
    user = request.user
    if user.is_authenticated:
        tasks = []
        taskList = TaskList.objects.all()
        username_auth = user.username
        for task in taskList:
            if task.username == username_auth:
                categories = TaskCategory.objects.all()
                statuses = TaskStatus.objects.all()
                for category in categories:
                    if task.category == category.id:
                        task.category = category.category_name
                for status in statuses:
                    if task.status == status.id:
                        task.status = status.status_name
                try:
                    if task.task[0] == '' or task.task[0] == '\n':
                        task.task.pop(0)
                except:
                    task.task = "Tom uppgift"
                tasks.append(task)
    else:
        return rdirect('login')
    return render(request, 'todo.html', {'tasks':tasks})

def toDoAdd (request):
    user = request.user
    if user.is_authenticated:
        categories_list = []
        categories = TaskCategory.objects.all()
        for category in categories:
            categories_list.append(category.category_name)
        return render(request, 'todoadd.html', {'categories': categories_list})
    else:
        return redirect('login')

def toDoAddApplier(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('taskname')
            category_name_get = request.POST.get('category')
            categories = TaskCategory.objects.all()
            for category in categories:
                if category.category_name == category_name_get:
                    category_name_get = category.id
            TaskList.objects.create(
                username = user.username,
                task = name,
                status = 1,
                category = category_name_get
            )
            return redirect('toDo')
        else:
            return redirect('toDoAdd')
    else:
        return redirect('login')

def categoryAdd (request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'todoadd.html')
    else:
        return redirect('login')

def categoryApplier (request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('categoryname')

            if request.POST.get('categoryname'):
                TaskCategory.objects.create(category_name = request.POST.get('categoryname'))
                return redirect('toDo')
            else:
                return redirect('categoryAdd')
        else:
            return redirect('categoryAdd')
    else: 
        return redirect('login')

def changeStatus(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            action = request.POST.get("action_btn")
            checked = request.POST.getlist("status[]")
            workingList = []
            taskList = TaskList.objects.all()
            username_auth = user.username
            for task in taskList:
                for check in checked:
                    check = int(check)
                    if task.username == username_auth and task.id == check:
                        workingList.append(task.id)
            for task in taskList:
                for work in workingList:
                    if task.id == work:
                        if action == "done":
                            task.status = 2
                            task.save()
                        elif action == "delete":
                            task.delete()

        return redirect('toDo')
    else:
        return redirect('login')

def changeTask(request, taskID):
    user = request.user
    if user.is_authenticated:
        taskList = TaskList.objects.all()
        categories_list = []
        categories = TaskCategory.objects.all()
        for category in categories:
            categories_list.append(category.category_name)
        for task in taskList:
            if task.id == taskID and user.username == task.username:
                currentcatid = task.category
                currentcategory = categories[currentcatid-1].category_name
                return render(request, 'todochange.html', {'task':task, 'currentcategory':currentcategory,'categories':categories_list})
        return redirect('toDo')
    else:
        return redirect('login')

def changeTaskApply(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get('newtaskname')
            taskID = request.POST.get('taskID')
            category_name_get = request.POST.get('category')
            categories = TaskCategory.objects.all()
            for category in categories:
                if category.category_name == category_name_get:
                    category_name_get = category.id
            status = request.POST.get('status')
            taskList = TaskList.objects.all()
            for task in taskList:
                if task.id == int(taskID):
                    task.task = name
                    task.category = category_name_get
                    task.status = int(status)
                    task.save()
        return redirect('toDo')
    else:
        return redirect('login')