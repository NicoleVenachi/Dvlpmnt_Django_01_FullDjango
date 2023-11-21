
from django.urls import path

from . import views #from this import views

urlpatterns = [
  path('', views.index, name='index'),
]