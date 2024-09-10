from django.urls import path
from . import views
from .views import signup_view
from .views import profile_page
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


# Home Page
urlpatterns  = [
	path('', views.index, name='index'),

        # Authetication routes
        path('signup/', signup_view, name='signup'),
        path('tasks/', views.task_list, name='task_list'),
        path('accounts/', include('django.contrib.auth.urls')),
        # The profile page 

        path('profile/',views.profile_page, name='profile_page'),
        path('project-in-progress/', views.project_in_progress_page, name='project_in_progress'),
        path('projects/', views.projects_page, name='projects'),
]
