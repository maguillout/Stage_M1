from django.shortcuts import render
from django.utils import timezone
from .models import Table
from django.contrib.auth import authenticate, login
import pandas as pd
from .forms import ConnexionForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Methods
def diseases():
	#update of diseases list
	tab1=pd.read_csv("/home/maelle/Bureau/Stage/application/interface/variantsViz/static/data/diseases.csv",sep="\t")
	d=tab1['Associated_disease']
	return d

# Create your views here.

def home(request):
    #tab = Table.objects.all() 
    return render(request,'variantsViz/base.html', {})


def welcome(request):
	return render(request,'variantsViz/welcome.html', {})

def initialisation(request):
	dis=diseases()
	associated_disease=dis.drop_duplicates()
	#lst_virt = [{'id': virt_id, 'val': virt}, ....]
	return render(request,'variantsViz/init.html', {'diseaseList': associated_disease})

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
	return render(request,'variantsViz/run.html', {})

@login_required
def account(request):
	tab1=pd.read_csv("/home/maelle/Bureau/Stage/application/interface/variantsViz/static/data/diseases.csv",sep="\t")
	rendu=tab1.to_html()
	return render(request,'variantsViz/account.html', {'res': rendu})


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet srenvoyé n'est pas None
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

def dire_bonjour(request):
    if request.user.is_authenticated():
        return HttpResponse("Salut, {0} !".format(request.user.username))
    return HttpResponse("Salut, anonyme.")
