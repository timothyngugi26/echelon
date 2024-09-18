from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Task
d8d7ac46c02f657b86675ce8ff92d3f1755268be

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username and password:
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response({'message': 'Account created successfully!'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid data'}, status=status.HTTP_404_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return Response({'message': 'Logged in Successfully'}, status=status.HTTP_200_OK)
    else:
<<<<<<< HEAD
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
from django.contrib.auth.decorators import login_required
from .models import Project, Milestone, Task
from .forms import ProjectForm, MilestoneForm, TaskForm


def project_list(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project_management/index.html', {'projects': projects})


def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    project = Project.object.get(pk=pk)
    milestones = project.milestones.all
    tasks = Task.objects.filter(milestone__project=project)
    return render(request, 'project_management/task_list.html', {'project': project, 'milestones': milestones, 'tasks': tasks})
=======
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_AUTHORIZED)
>>>>>>> d8d7ac46c02f657b86675ce8ff92d3f1755268be
