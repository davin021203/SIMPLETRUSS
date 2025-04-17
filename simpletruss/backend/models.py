from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    
    def serialize(self):
        if self.priority == 0:
            priority = 'Low'
        elif self.priority == 1:
            priority = 'Medium'
        elif self.priority == 2:
            priority = 'High'
        return {
            'id': self.id,
            'name': self.name,
            'desc': self.description,
            'priority': priority,
            'due': self.due_date
        }