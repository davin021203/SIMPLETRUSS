from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_view/', views.login_view.as_view(), name='login_view'),
    path('register/', views.register, name='register'),
    path('gettask/', views.get_task, name='get_all_task'),
    path('gettask/<str:taskname>/', views.get_task, name='get_task_by_name'),
    path('create_task/', views.create_task, name='create_task'),
]