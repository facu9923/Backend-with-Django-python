from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def hello(request):
    title='wlcome to course of django'
    return render(request, 'index.html', {'title': title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{'tasks':tasks} )

@csrf_exempt
def create_tasks(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST['title'], description = request.POST['description'], project_id=1)
        return redirect('/tasks/')
        
    return render(request, 'create_tasks.html', {'form':CreateNewTask})

@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        Project.objects.create(title=request.POST['title'])
        return redirect('/projects/')

    return render(request, 'create_project.html', {'form': CreateNewProject})