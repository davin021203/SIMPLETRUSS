from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('addtask/', views.add_new_task_page, name='next_page'),
    path('get-tasks/', views.get_tasks, name='get_tasks'),
    path('add-task/', views.add_new_task_page, name='next_page'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
