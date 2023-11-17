from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature# import de los models 


# Create your views here.
def index(request):
  # return HttpResponse('<h1>Welcome </h1>')

  features = Feature.objects.all() # R-ead all
  context = {
    'features': features
  }

  return render(request, 'index.html', context)


def register(request):

  #POST methods routing for this view
  if request.method == 'POST':
    username = request.POST.get('username')  
    email = request.POST.get('email')  
    password = request.POST.get('password')  
    password2 = request.POST.get('password2')  

    #verifco passwords are equal
    if password == password2:


    #almaceno data en DB (moder user que es el by default)

  return render(request, 'register.html') #si lo acceso normal, simplemlente traigo el html

def counter(request):

  text = request.POST.get('text')

  textToArray = text.split() # (), empyt, thencesplit by white spacing
  
  context = {
    'amount': len(textToArray) #amountOfWords
  }

  return render(request, 'counter.html', context) #html for counter

