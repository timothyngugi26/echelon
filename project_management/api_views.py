from rest_framework import viewsets
from rest_framework.response import Response
from .models import Project, Milestone, Task
from .serializers import ProjectSerializer, MilestoneSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset =Task.objects.all()
    serializer_class = TaskSerializer

class ProjectMilestonesViewSet(viewsets.ViewSet):
    def list(self, request, project_id):
        milestones = Milestone.objects.filter(project_id=project_id)
        serializer = MilestoneSerializer(milestones, many=True)
        return Response(serializer.data)

class MilestoneTasksViewSet(viewsets.ViewSet):
    def list(self, request, milestone_id):
        tasks = Task.objects.filter(milestone_id=milestone_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
