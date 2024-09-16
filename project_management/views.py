from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Milestone, Task
from .forms import ProjectForm, MilestoneForm, TaskForm


def index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'project_management/base.html', {'projects': projects})


def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    project = Project.object.get(pk=pk)
    milestones = project.milestones.all
    tasks = Task.objects.filter(milestone__project=project)
    return render(request, 'project_management/task_list.html', {'project': project, 'milestones': milestones, 'tasks': tasks})
