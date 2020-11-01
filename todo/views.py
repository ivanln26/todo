from django.db import models
from django.shortcuts import render, redirect

from .forms import ToDoForm
from .models import ToDo

def index(request):
    todos = ToDo.objects.order_by('-created_at')
    todoform = ToDoForm()
    ctx = {'todos': todos, 'todoform': todoform}
    return render(request, "index.html", ctx)

def todo(request):
    content = request.POST.get('content')
    todo = ToDo(content=content)
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def archive(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.is_archived = True
    todo.save()
    return redirect('index')
