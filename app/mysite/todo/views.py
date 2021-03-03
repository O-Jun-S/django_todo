from .models import Task
from .forms import TaskForm

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {"tasks": Task.objects.all()})

def read(request, task_id):
    return render(request, "todo/read.html", {"task": Task.objects.get(id=task_id)})
