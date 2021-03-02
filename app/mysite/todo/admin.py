from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "text")}),
        ("Created date", {"fields": ("created_date",)},)
    )


admin.site.register(Task, TaskAdmin)
