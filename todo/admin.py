from django.contrib import admin

from .models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):

    list_display = ('content', 'is_archived', 'created_at', 'updated_at',)
    list_filter = ('is_archived',)
