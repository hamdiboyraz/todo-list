from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/') # Should be '/', not ''

    context = {'tasks':tasks, 'form':form}
    return render(request, 'list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task) # Instance provides retrieving same item 

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'update_task.html', context)

def deleteTask(request, pk):
    task  = Task.objects.get(id=pk) # get item by id-primary key

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'item':task} # refers to {{ item }} in delete.html
    return render(request, 'delete.html', context)

def done(request, pk):
    item  = Task.objects.get(id=pk)
    
    if item.complete == True:
        item.complete = False
    else:
        item.complete = True
    item.save()
    
    return redirect('/')

