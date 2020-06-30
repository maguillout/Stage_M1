from django.shortcuts import render
from django.utils import timezone
from .models import Table


# Create your views here.

def home(request):
    #tab = Table.objects.all() 
    return render(request,'variantsViz/base.html', {})

def welcome(request):
	return render(request,'variantsViz/welcome.html', {})

def initialisation(request):
	return render(request,'variantsViz/init.html', {})

def login(request):
	tabs = Table.objects.all()
	return render(request,'variantsViz/login.html', {'tabs': tabs})

def logout(request):
	return render(request,'variantsViz/logout.html', {})

def analysis(request):
	return render(request,'variantsViz/analysis.html', {})

def database(request):
	return render(request,'variantsViz/database.html', {})

def running(request):
	return render(request,'variantsViz/running.html', {})