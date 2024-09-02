from django.urls import path
from . import views

urlpatterns  = [
	path('', views.index, name='index'), #demo route
        path('tasks/', views.task_list, name='task_list'),
]
