from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projets=Project.objects.all()
    return render(request,'home.html',{'projects':projets})