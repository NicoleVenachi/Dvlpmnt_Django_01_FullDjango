from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Home</h1>")

  print(request.user)
  return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
  return HttpResponse("<h1>contact</h1>")

def about_view(request, *args, **kwargs):

  context = {
    "text": "This is about us",
    "number": 123,
    "listElems": [123, 345, 567]
  }
  return render(request, "about.html", context)

def social_view(request, *args, **kwargs):
  return HttpResponse("<h1>social</h1>")