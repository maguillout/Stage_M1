from django.urls import path
from . import views

from django.conf.urls import include, url

#from .views import pathology_upload

urlpatterns = [
	path('', views.welcome, name='welcome'), 
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),   
    path('initialisation/', views.initialisation, name='initialisation'),
    path('running/', views.running, name='running'),
    path('analysis/', views.analysis, name='analysis'),
    path('database/', views.database, name='database'),
    path('account/', views.account, name='account'),
    path('pathologies/<int:id>', views.displayPathology, name='displayPathology'),
#    path('contact/', views.nouveau_contact, name='nouveau_contact'),
	path('pathologies/', views.pathology_upload, name='pathology_upload'),
	path('genes/', views.genes_upload, name='genes_upload'),
#	path('register/', views.register, name='register'),
]
