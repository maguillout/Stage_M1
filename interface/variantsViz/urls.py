from django.urls import path
from . import views

urlpatterns = [
    path('tab_list/', views.tab_list, name='tab_list'),
]
