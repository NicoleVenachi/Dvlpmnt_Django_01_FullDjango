
from django.urls import path 
from . import views #importo views de este mismo forde

urlpatterns = [
  path('', views.index, name = 'index'), # (path, handler), '' es la root
  path('counter', views.counter, name = 'counter'),
  path('register', views.register, name = 'register') #add route for registre
]

