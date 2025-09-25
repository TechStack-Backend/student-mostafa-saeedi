from django.shortcuts import render
from .models import Developer, Project
from .forms import DeveloperForm, ProjectForm

def developers_list(request):
    developers = Developer.objects.all()
    return render(request, 'core/developers.html', {'developers': developers})

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects})

def add_developer(request):
    if request.method == 'POST':
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DeveloperForm()
    return render(request, 'core/add_developer.html', {'form': form})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProjectForm()
    return render(request, 'core/add_project.html', {'form': form})
