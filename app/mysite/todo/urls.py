from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index),
    path("read/<int:task_id>", views.read)
]
