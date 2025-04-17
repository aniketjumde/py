from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        new_task = request.POST.get('title')
        if new_task:
            Task.objects.create(title=new_task)
        return redirect('/')
    return render(request, 'todo/index.html', {'tasks': tasks})
