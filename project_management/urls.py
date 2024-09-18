from . import views
from .views import signup_view, CustomTokenObtainPairView
# from .views import profile_page, index
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns  = [
	# Home Page
        # path('', views.index, name='index'),

        # Authetication routes
        path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/signup/', signup_view, name='signup'),
        
        # API routes
        path('api/', include('project_management.api_urls')),
        
        #  Django views
        # path('profile/',views.profile_page, name='profile_page'),
        # path('project-in-progress/', views.project_in_progress_page, name='project_in_progress'),
        # path('projects/', views.projects_page, name='projects'),
]
