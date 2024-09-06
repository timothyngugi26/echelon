from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns  = [
	path('', views.index, name='index'), #demo route
        path('login/', views.login_view, name='login'),
        path('signup/', views.signup_view, name='signup'),
        path('tasks/', views.task_list, name='task_list'),
]

#The profile page 
urlpatterns = [
    path('profile/', views.profile_page, name='profile_page'),
    path('projects/', views.projects_page, name='projects'),
    path('project-in-progress/', views.project_in_progress_page, name='project_in_progress'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_management/', include('project_management.urls')),
]

