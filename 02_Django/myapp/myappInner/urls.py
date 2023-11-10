
from django.urls import path 
from . import views #importo views de este mismo forde

urlpatterns = [
  path('', views.index, name = 'index'), # (path, handler), '' es la root
]

