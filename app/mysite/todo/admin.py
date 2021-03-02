from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ["title", "text"]


admin.site.register(Task, TaskAdmin)
