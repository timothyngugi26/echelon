from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.http import HttpResponse

def profile_page(request):
    return render(request, 'profile_page.html')


def index(request):
     form = AuthenticationForm()
     return render(request, 'project_management/index.html',  {'form': form})


def login_view(request):
    if request.method  == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_page')
            else:
                form.add_error(None, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    # print("Entering signup_view")
    # return HttpResponse("The view works!")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # print("User signed up and logged in")
            return redirect('profile_page')
        else:
            print('Invalid form')
    else:
        form = UserCreationForm()
        
    return render(request, 'project_management/signup.html', {'form': form})

def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    tasks = Task.objects.all()
    return render(request, 'project_management/task_list.html', {'tasks': tasks})

def profile_page(request):
    return render(request, 'project_management/profile_page.html')

def projects_page(request):
    return render(request, 'project_management/projects.html')

def project_in_progress_page(request):
    return render(request, 'project_management/project_in_progress.html')
