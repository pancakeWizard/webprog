from django.shortcuts import render
from . models import TaskList, TaskCategory, TaskStatus
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse 

# Create your views here.
def toDo(request):
    """
    En funktion som tar information om användarens uppgifter från databasen
    om användaren är auktoriserad. Sedan skickas info vidare till template.
    Om användare inte loggat in då ska funktionen redirecta användare till
    inloggnin sida.
    """
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
    """
    Funktionen låter användare lägga till en uppgift om användare är inloggad. Annars redirectar till inloggning.
    Skickar en lista med alla kategorier till template.
    """
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
    """
    Funktionen bearbetar form från template av toDoAdd funktionen.
    Funktionen tar emot info och sparar den i databas och därefter
    redirectar användare vidare till to-do-lista.
    Om användare inte är inloggad så ska den redirectas till 
    logga in sida.
    """
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
    """
    Funktionen visar template med form för att lägga till 
    kategori om anvädare är inloggad. Annars redirectas 
    användare till logga in.
    """
    user = request.user
    if user.is_authenticated:
        return render(request, 'todoadd.html')
    else:
        return redirect('login')

def categoryApplier (request):
    """
    Funktionen bearbetar form från categoryAdd.
    Ny kategori sparas i databas och sedan redirectas
    användare till sin to-do-lista.
    Om man inte skriver in någon symbol som namn på kategorin så
    kommer användare att redirectas till categoryAdd igen.
    Detta görs för att undvika tomma kategorier.
    """
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
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
    """
    Denna funktion bearbetar en form från toDo sidan.
    Om man markerar en eller några uppgifter så ska
    man kunna ändra läge till slutfört eller ta bort
    de uppgifterna. Sedan redirectas man tillbaka till
    uppdaterade versionen av toDo. Om man inte inloggad
    så ska man redirectas till logga in.
    """
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
                        workingList.appendwq
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
    """
    Funktionen tar allt information om en uppgift
    man vill ändra och erbjuder möjlighet att ändra den.
    Som standardvärde används det de värde som finns nu
    i databasen. De skickas till html.
    Om användare inte är inloggat så ska den redirectas till logga in.
    Om man inte har några uppgifter men ändå når urlen så ska den
    redirectas till toDo sidan.

    """
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
    """
    Funktionen bearbetar form från changeTask.
    User input uppdaterar info i databas och
    skickar användare till toDo.
    Om användare inte är inloggat så ska funktionen
    redirecta till logga in.
    """
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