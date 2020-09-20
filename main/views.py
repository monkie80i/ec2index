from django.shortcuts import render
from .models import Project

# Create your views here.
def index_view(request):
	return render(request,'index.html')

def projects(request):
	projects = Project.objects.filter(active=True)
	template = "projects.html"
	return render(request,template,{'projects':projects})