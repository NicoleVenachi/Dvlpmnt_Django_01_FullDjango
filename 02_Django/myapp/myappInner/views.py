from django.shortcuts import render
from django.http import HttpResponse

from .models import Feature# import de los models 


# Create your views here.
def index(request):
  # return HttpResponse('<h1>Welcome </h1>')
  feature1 = Feature() # creo un objeto de ese tipo de datos einicializo sus valores
  feature1.id = 0
  feature1.name = 'Fast'
  feature1.details = 'Our services is very quick'
  feature1.is_true = False

  feature2 = Feature() # creo un objeto de ese tipo de datos einicializo sus valores
  feature2.id = 1
  feature2.name = 'Fast'
  feature2.details = 'Our services is very quick'
  feature2.is_true = True

  feature3 = Feature() # creo un objeto de ese tipo de datos einicializo sus valores
  feature3.id = 2
  feature3.name = 'Fast'
  feature3.details = 'Our services is very quick'
  feature3.is_true = False

  feature5 = Feature() # creo un objeto de ese tipo de datos einicializo sus valores
  feature5.id = 3
  feature5.name = 'Fast'
  feature5.details = 'Our services is very quick'
  feature5.is_true = True

  features = [feature1, feature2, feature3, feature5]
  context = {
    'features': features
  }

  return render(request, 'index.html', context)

def counter(request):

  text = request.POST.get('text')

  textToArray = text.split() # (), empyt, thencesplit by white spacing
  
  context = {
    'amount': len(textToArray) #amountOfWords
  }

  return render(request, 'counter.html', context) #html for counter

