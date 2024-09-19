from . import views
from .views import signup, login,  CustomTokenObtainPairView
from .api_views import ProjectViewSet, MilestoneViewSet, TaskViewSet, ProjectMilestonesViewSet, MilestoneTasksViewSet
# from .views import profile_page, index
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns  = [
    
        # path('', views.index, name='index'),
        path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/signup/', views.signup, name='signup'),
        path('api/login/', views.login, name='login'),
        # API routes
        path('api/projects/<int:project_id>/milestones/', ProjectMilestonesViewSet.as_view),
        path('api/milestones/<int:mileston_id>/tasks/', MilestoneTasksViewSet.as_view({'get': 'list'}), name='milestone-tasks'),
        path('api/', include('project_management.api_urls')),
]
