from .models import Task

from django.utils import timezone
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["limit_date", "title", "text"]
