from django.urls import path
from . import views


urlpatterns = [
	path('', views.welcome, name='welcome'), 	
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),   
    path('initialisation/', views.initialisation, name='initialisation'),
    path('running/', views.running, name='running'),
    path('analysis/', views.analysis, name='analysis'),
    path('database/', views.database, name='database'),
    path('account/', views.account, name='account'),
    path('new_pathology/', views.new_patho, name='new_patho'),

]

