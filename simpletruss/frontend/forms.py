from django import forms
from datetime import date, datetime, time
from .models import Task

class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        (2, 'High'),
        (1, 'Medium'),
        (0, 'Low'),
    ]

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Priority"
    )

    class Meta:
        model = Task
        fields = ['name', 'desc', 'priority', 'due_date']
        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_date = date.today().isoformat()
        self.fields['due_date'].widget.attrs['min'] = min_date

    def clean_due_date(self):
        user_date = self.cleaned_data['due_date']
        return datetime.combine(user_date, time.min) 
