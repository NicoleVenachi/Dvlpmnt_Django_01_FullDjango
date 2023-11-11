from django.shortcuts import render
from django.http import HttpResponse

from .models import Feature# import de los models 


# Create your views here.
def index(request):
  # return HttpResponse('<h1>Welcome </h1>')

  features = Feature.objects.all() # R-ead all
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

