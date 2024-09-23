from rest_framework.routers import DefaultRouter
from .api_views import ProjectViewSet, MilestoneViewSet, TaskViewSet, ProjectMilestonesViewSet, MilestoneTasksViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'milestones', MilestoneViewSet, basename='milestones')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = router.urls
