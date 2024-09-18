from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, MilestoneViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'milestones', MilestoneViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
        path('', include(router.urls)),
]
