from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.

def hello(request):
    title='wlcome to course of django'
    return render(request, 'index.html', {'title': title})

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {'projects': projects})

def tasks(request):
    # tasks = list(Task.objects.values())
    task = list(Task.objects.values())
    return render(request, 'tasks.html',{'tasks':task} )
