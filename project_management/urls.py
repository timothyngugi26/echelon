from django.urls import path
from . import views

urlpatterns  = [
	path('', views.index, name='index'), #demo route
        path('login/', views.login_view, name='login'),
        path('signup/', views.signup_view, name='signup'),
        path('tasks/', views.task_list, name='task_list'),
]
