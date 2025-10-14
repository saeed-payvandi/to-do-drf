from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.ToDo)
class ToDoAdmin(admin.ModelAdmin):
    pass