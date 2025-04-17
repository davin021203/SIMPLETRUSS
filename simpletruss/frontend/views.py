from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404



# Create your views here.
def index(request):
    return render(request, 'frontend/index.html')

def add_new_task_page(request):
    return render(request, 'frontend/addnewtask.html')

def task_list(request):
    return render(request, 'frontend/task_list.html')

def get_tasks(request):
    tasks = [
        {'id': 1, 'name': 'Do laundry', 'desc': 'Wash clothes', 'priority': 'High', 'due': '2025-04-20'},
        {'id': 2, 'name': 'Buy groceries', 'desc': 'Milk, eggs, bread', 'priority': 'Medium', 'due': '2025-04-18'},
    ]
    return JsonResponse(tasks, safe=False)  

def add_new_task_page(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  
    else:
        form = TaskForm()

    return render(request, 'frontend/addnewtask.html', {'form': form})



def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'frontend/edittask.html', {'form': form, 'task_id': task_id})
