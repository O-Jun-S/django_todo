from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "text")}),
        ("Date Data", {"fields": ("created_date", "limit_date",)},),
    )


admin.site.register(Task, TaskAdmin)
