from .models import Task
from .forms import TaskForm

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {"tasks": Task.objects.all()})


def create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = TaskForm()

    return render(request, "todo/create.html", {"form": form})
