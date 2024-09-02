from django.shortcuts import render

def index(request):
    return render(request, 'project_management/index.html')

def task_list(request):
    # Fetch tasks from the database (assuming a Task model exists)
    tasks = Task.objects.all()
    return render(request, 'project_management/task_list.html', {'tasks': tasks})
