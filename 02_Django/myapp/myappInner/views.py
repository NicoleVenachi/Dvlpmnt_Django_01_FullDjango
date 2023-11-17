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
      # check if the email/user exists on the db
      if User.objects.filter(email=email).exists():
        messages.info(request, 'Email already exists') #send back an error message
        return redirect('register') # route back to register
      
      elif User.objects.filter(username=username).exists:
        messages.info(request, 'Username already used') #send back an error message
        return redirect('register') # route back to register
      
      else: #almaceno data en DB (en model User)

        user = User.objects.create_user(username=username, email=email, password=password) #creo user con ese modelo
        
        user.save() # almaceno el user

        return redirect('login') # route  to login
    
    else:
      messages.info(request, 'Passwords do not match') #send back an error message
      return redirect('register') # route back to register

  else: #for a normal request on the page (e.g., HTTP)
    return render(request, 'register.html') #si lo acceso normal, simplemlente traigo el html

def counter(request):

  text = request.POST.get('text')

  textToArray = text.split() # (), empyt, thencesplit by white spacing
  
  context = {
    'amount': len(textToArray) #amountOfWords
  }

  return render(request, 'counter.html', context) #html for counter

