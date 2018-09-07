from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('todo', views.todo, name="todo"),
    path('delete/<int:todo_id>', views.delete, name="delete"),
    path('archive/<int:todo_id>', views.archive, name="archive")
]