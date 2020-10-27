from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import authenticate, login
import pandas as pd
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
from random import randint
from .models import Pathology


# Methods

# Create your views here.

def home(request):
    #tab = Table.objects.all() 
    return render(request,'variantsViz/base.html', {})


def welcome(request):
	return render(request,'variantsViz/welcome.html', {})

def initialisation(request):
	associated_disease=Pathology.objects.order_by('name')
	return render(request,'variantsViz/init.html', {'diseaseList': associated_disease})

def login(request):
	return render(request,'variantsViz/login.html', {})


def logout(request):
	return render(request,'variantsViz/logout.html', {})


def analysis(request):
	return render(request,'variantsViz/analysis.html', {})


def database(request): #request for the page "database"
    patho = Pathology.objects.order_by('name') #calling of all the recorded Pathologys
    return render(request,'variantsViz/database.html', {'patho': patho}) 
    #display the html file and returns the variable which contains the Pathologys list

def running(request):
	return render(request,'variantsViz/run.html', {})

@login_required
def account(request):
    tab1=pd.read_csv("/home/maelle/Bureau/Stage/application/interface/variantsViz/static/data/disease-genes.csv",sep=";")    
    #tab1=pd.read_csv("/home/maelle/Documents/Nextcloud/application/interface/variantsViz/static/data/disease-genes.csv",sep=";")    
    rendu=tab1.to_html()
    return render(request,'variantsViz/account.html', {})


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'variantsViz/account.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

from django.http import HttpResponse


from .forms import newPatho

def new_patho(request):
    patho = newPatho()
    return render(request, 'variantsViz/new_patho.html', {'patho':patho})

