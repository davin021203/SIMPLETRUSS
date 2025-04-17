from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('addtask/', views.add_new_task_page, name='next_page'),
    path('get-tasks/', views.get_tasks, name='get_tasks'),
    path('add-task/', views.add_new_task_page, name='next_page'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
]
