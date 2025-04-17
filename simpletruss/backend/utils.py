# backend/utils.py

from .models import Task

def get_user_tasks(user, taskname=None, sort=None):
    if not user.is_authenticated:
        return None  # or raise an exception

    if taskname:
        try:
            return [Task.objects.get(name=taskname, user=user)]
        except Task.DoesNotExist:
            return []

    tasks = Task.objects.filter(user=user).order_by('-created_at')
    if sort == 'asc':
        tasks = tasks.order_by('-priority')
    elif sort == 'desc':
        tasks = tasks.order_by('priority')

    return tasks
