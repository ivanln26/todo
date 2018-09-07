from django.shortcuts import render, redirect
from django.db import models
from .models import ToDo
from .forms import ToDoForm

def index(request):
    todos = ToDo.objects.order_by('-date')
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