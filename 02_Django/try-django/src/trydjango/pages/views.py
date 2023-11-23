from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
  return HttpResponse("<h1>Home</h1>")

def contact_view(request, *args, **kwargs):
  return HttpResponse("<h1>contact</h1>")

def about_view(request, *args, **kwargs):
  return HttpResponse("<h1>about</h1>")

def social_view(request, *args, **kwargs):
  return HttpResponse("<h1>social</h1>")