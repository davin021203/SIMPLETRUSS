from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from .models import Task
from rest_framework.views import APIView 
from .utils import get_user_tasks
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return JsonResponse({"message": "Hello, world!"})

class login_view(APIView):
    def post(self, request):
        # Handle login logic here
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
            
def login(request):
    if request.method == 'POST':
        # Handle login logic here  
        username = 'admin'
        password = '1234'
        
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
    else:
        return JsonResponse({"message": "Request method not allowed"}, status=405)
    
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
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    sort = request.GET.get('sort', None)
    tasks = get_user_tasks(request.user, taskname, sort)

    if taskname and not tasks:
        return JsonResponse({"error": "Task not found"}, status=404)

    serialized = [task.serialize() for task in tasks]
    return JsonResponse(serialized if not taskname else serialized[0], safe=not taskname)
    
@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        user = request.user

        if not user.is_authenticated:
            return JsonResponse({"error": "User not authenticated"}, status=401)

        task = Task.objects.create(
            name=name,
            description=desc,
            priority=priority,
            due_date=due_date,
            user=user
        )
        return JsonResponse({"message": "Task created successfully!"}, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)
    
def delete_task(request, task_id):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return JsonResponse({"message": "Task deleted successfully!"}, status=200)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)