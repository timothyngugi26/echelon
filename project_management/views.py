from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Task, Project, Milestone
from django.http import JsonResponse

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@api_view(['POST'])
def test_view(request):
    return JsonResponse({"message": "POST request recieved"},status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if username and password:
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            refresh =  RefreshToken.for_user(user)
            return JsonResponse({
                'message': 'Account created successfully!',
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED) 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        if not (username and password):
            return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_404_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'message': 'Logged in Successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    else:

        return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
