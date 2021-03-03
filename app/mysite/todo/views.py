import datetime

from .models import Task
from .forms import TaskForm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "todo/index.html", {"tasks": Task.objects.all()})


def read(request, task_id):
    return render(request, "todo/read.html", {"task": Task.objects.get(id=task_id)})


def create(request):
    return render(request, "todo/create.html", {"form": TaskForm})


def create_task(request):
    title = request.POST["title"]
    task = Task()
    task.title = title
    date_lst = list(map(int, request.POST["limit_date"].split("/")))
    task.limit_date = datetime.datetime(year=date_lst[0], month=date_lst[1], day=date_lst[2])
    task.save()
    return HttpResponseRedirect(reverse('read', args=[task.id]))
