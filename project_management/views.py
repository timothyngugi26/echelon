from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render

def profile_page(request):
    return render(request, 'profile_page.html')


def index(request):
     form = AuthenticationForm()
     return render(request, 'project_management/index.html',  {'form': form})


def login_view(request):
    if request.method  == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
           # user = form.get_user()
           # login(request, user)
            # return redirect('home')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('signup')
        else:
            form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'project_management/signup.html')

def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    tasks = Task.objects.all()
    return render(request, 'project_management/task_list.html', {'tasks': tasks})

def profile_page(request):
    return render(request, 'profile_page.html')

def projects_page(request):
    return render(request, 'projects.html')

def project_in_progress_page(request):
    return render(request, 'project_in_progress.html')
