from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from backend.utils import get_user_tasks
from django.contrib import messages
import requests
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

@login_required(login_url='/login/')
def add_new_task_page(request):
    return render(request, 'frontend/addnewtask.html')

@login_required(login_url='/login/')
def task_list(request):
    return render(request, 'frontend/task_list.html')

@login_required(login_url='/login/')
def get_tasks(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    sort = request.GET.get('sort', None)
    tasks = get_user_tasks(request.user, sort=sort)
    serialized = [task.serialize() for task in tasks]

    return JsonResponse(serialized, safe=False)

@login_required(login_url='/login/')
def add_new_task_page(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Prepare data to send to backend
            task_data = {
                'name': form.cleaned_data['name'],
                'desc': form.cleaned_data['desc'],
                'priority': form.cleaned_data['priority'],
                'due_date': form.cleaned_data['due_date'],  
            }
            # Send POST request to backend
            response = requests.post('http://127.0.0.1:8000/api/create_task/', data=task_data, cookies=request.COOKIES)

            if response.status_code == 201:
                messages.success(request, "Task created!")
                return redirect('frontend:task_list')
            else:
                messages.error(request, "Failed to create task.")
    else:
        form = TaskForm()

    return render(request, 'frontend/addnewtask.html', {'form': form})

@login_required(login_url='/login/')
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('frontend/task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'frontend/edittask.html', {'form': form, 'task_id': task_id})

def login(request):
    return render(request, 'frontend/login.html')
def register(request):
    return render(request, 'frontend/register.html')