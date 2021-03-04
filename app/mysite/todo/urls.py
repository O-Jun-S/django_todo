from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("index", views.index, name="index"),
    path("read/<int:task_id>", views.read, name="read"),
    path("create", views.create, name="create"),
    path("create_task", views.create_task, name="create_task"),
]
