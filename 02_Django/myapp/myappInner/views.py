from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse('<h1>Welcome </h1>')

  context = {
    'name': 'Maria',
    'age': 25,
    'nationality': 'British',
  }
  
  return render(request, 'index.html', context)

def counter(request):

  text = request.POST.get('text')

  textToArray = text.split() # (), empyt, thencesplit by white spacing
  
  context = {
    'amount': len(textToArray) #amountOfWords
  }

  return render(request, 'counter.html', context) #html for counter

