from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_filter = ('archived',)

admin.site.register(ToDo, ToDoAdmin)