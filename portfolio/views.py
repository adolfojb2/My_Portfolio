from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() #Trae todos los proyectos
    return render(request, 'home.html',{'projects':projects})
