from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    form = AuthenticationForm()
    return render(request, 'project_management/index.html',  {'form': form})


def login_view(request):
    if request.method  == 'POST':
        pass
    return render(request, 'project_management/login.html')

def signup_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'project_management/signup.html')

def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    tasks = Task.objects.all()
    return render(request, 'project_management/task_list.html', {'tasks': tasks})
