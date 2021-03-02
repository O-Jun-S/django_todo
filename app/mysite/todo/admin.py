from django.contrib import admin
from .models import Task


# Register your models here.
#class TaskAdmin(admin.ModelAdmin) {
#    fieldsets = [
#        (None, {"fields": ["title"]}),
#        (None, {"fields": ["text"]})
#    ]
#}


admin.site.register(Task)
