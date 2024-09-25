from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.recomendations, name='recomendations'), 
]
