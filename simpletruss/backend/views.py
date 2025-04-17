from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from .models import Task
from rest_framework.views import APIView 
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

# Create your views here.
def index(request):
    return JsonResponse({"message": "Hello, world!"})

class login_view(APIView):
    def post(self, request):
        # Handle login logic here
        return JsonResponse({"message": "Login successful!"})
    def get(self, request):
        # Handle GET request for login
        return JsonResponse({"message": "GET request for login"})
        '''
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                'username': user.username
            }, status=200)
        else:
            return JsonResponse({
                'error': True,
                'message': 'Invalid username and/or password'
            }, status=409)
            '''
@csrf_exempt            
def login(request):
    if request.method == 'POST':
        # Handle login logic here  
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not username or not password:   
            return JsonResponse({
                'error': True,
                'message': 'Username and password are required'
            }, status=400)
        # Check if user exists and authenticate 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('frontend:task_list'))
        else:
            return JsonResponse({
                'error': True,
                'message': 'Invalid username and/or password'
            }, status=409)
        
    else:
        return HttpResponseRedirect(reverse('frontend:task_list'))
def register(request):
    if request.method == 'POST':
        # Handle registration logic here
        return JsonResponse({"message": "Registration successful!"})
    else:
        return JsonResponse({"message": "Registration page"})

def logout(request):
    # Handle logout logic here
    logout(request)
    return HttpResponseRedirect('/')    

def get_task(request, taskname=None):
    # Handle getting a task by ID
    if request.user.is_authenticated:
        sort = request.GET.get('sort', None)
        if taskname:
            try:
                task = Task.objects.get(name=taskname, user=request.user)
                return JsonResponse(task.serialize(), status=200)
            except Task.DoesNotExist:
                return JsonResponse({"error": "Task not found"}, status=404)
            
        tasks = Task.objects.filter(user=request.user).order_by('-created_at')
        if sort == 'asc':
            tasks = tasks.order_by('-priority')
        elif sort == 'desc':
            tasks = tasks.order_by('priority')
            
        serialized_tasks = [task.serialize() for task in tasks]
        return JsonResponse(serialized_tasks, safe=False)
    else:
        return JsonResponse({"error": "User not authenticated"}, status=401)
    
    
def create_task(request):
    if request.method == 'POST':
        # Handle creating a task
        data = request.POST
        
        return JsonResponse({"message": "Task created successfully!"})
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
    