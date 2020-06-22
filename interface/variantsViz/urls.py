from django.urls import path
from . import views

urlpatterns = [
    path('', views.tab_list, name='tab_list'),
]
