from . import views
from .views import signup, login,  CustomTokenObtainPairView
from .api_views import ProjectViewSet, MilestoneViewSet, TaskViewSet, ProjectMilestonesViewSet, MilestoneTasksViewSet
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns  = [
    
        # JWT token routes
        path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        # API routes for signup and login
        path('api/signup/', views.signup, name='signup'),
        path('api/login/', views.login, name='login'),
        
        # API routes for project milestones and tasks
        path('api/projects/<int:project_id>/milestones/', ProjectMilestonesViewSet.as_view({'get': 'list'}), name='project-milestones'),
        path('api/milestones/<int:milestone_id>/tasks/', MilestoneTasksViewSet.as_view({'get': 'list'}), name='milestone-tasks'),
        # path('', include('project_management_frontend.urls')),
        path('api/', include('project_management.api_urls')),
]
