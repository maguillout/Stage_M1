from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
import pandas as pd
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
from random import randint
from .models import Pathology, Job, Gene, Variant, Patient
from pathlib import Path
import os

# Methods

# Create your views here.

def home(request):
    #tab = Table.objects.all() 
    return render(request,'variantsViz/base.html', {})

from django.contrib import messages



def welcome(request):
#    messages.success(request, 'Student created successfully.')
	return render(request,'variantsViz/welcome.html',{})

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
    tab_id = pd.read_csv('/home/maelle/Bureau/Stage/application/interface/variantsViz/static/data/mim2gene.csv',sep=";")
    truc = tab_id[tab_id['Ensembl_id'].str.find("ENSG00000003400")==0]['Approved_Symbol']
    return render(request,'variantsViz/account.html', {'t': truc})

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

from django.http import HttpResponse

def displayPathology(request, id):
    try:
        patho = Pathology.objects.get(id=id)
    except Pathology.DoesNotExist:
        raise Http404
    return render(request, 'variantsViz/pathology.html', {'patho': patho})

def displayGene(request, id):
    try:
        gene = Gene.objects.get(id=id)
    except Gene.DoesNotExist:
        raise Http404
    return render(request, 'variantsViz/genes.html', {'gene': gene})


from django.shortcuts import render, get_object_or_404, redirect
import csv, io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

def pathology_upload(request):
    prompt = {
    'order': 'Upload a csv file which contains several pathologies'
    }
    if request.method == 'GET':
        return render(request, 'variantsViz/pathologies.html', prompt)
    else:
        csv_file = request.FILES["file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a csv file')
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=';', quotechar="\""):
            created = Pathology.objects.update_or_create(
                name = column[0],
                associated_gene_OMIM = column[1],
                infos = column[2]
                )
        return render(request,"variantsViz/pathologies.html", {})


def genes_upload(request):   
    current_path = Path(os.getcwd())
    file_path = (f'{current_path.parent}/interface/variantsViz/static/data/mim2gene.csv')
    tab_id = pd.read_csv(file_path,sep=";")
    truc = ""
    prompt = {'order': truc}
    if request.method == 'GET':
        return render(request, 'variantsViz/genes.html', prompt)
    else:
        csv_file = request.FILES["file"]
        data_set = csv_file.read().decode('UTF-8')# setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        tab = pd.read_csv('csv_file',sep=';s')
        for column in csv.reader(io_string, delimiter=';', quotechar="\""):
            created = Pathology.objects.update_or_create(
                name = column[0],
                infos = column[2]
                )
        return render(request,"variantsViz/genes.html", {})


