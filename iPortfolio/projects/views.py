from django.shortcuts import render
from .models import Projects
# Create your views here.

def projects(request):  
    return render(request, 'projects/projects.html', {"proj" : Projects.objects.all()})

def web_project(request):
    return render(request, 'projects/web_project.html', {"proj" : Projects.objects.all()})

def game_project(request):
    return render(request, 'projects/game_project.html', {"proj" : Projects.objects.all()})

def block_project(request):
    return render(request, 'projects/block_project.html', {"proj" : Projects.objects.all()})

def front(request):
    return render(request, 'projects/front.html', {"proj" : Projects.objects.all()})

# def workstation(request):
#     return render(request, 'workstation/works.html', {"work": Projects.objects.all()})