from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    tasks= Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'task':tasks, 'form' :form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    i = Task.objects.get(id = pk) 
    
    form = TaskForm(instance=i)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=i)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form' :form}
    return render(request, 'update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    context= {'item':item}
    return render(request,'delete.html',context)