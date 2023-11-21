
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'), # rooms templates routing
    path('checkview', views.checkview, name='checkview'), # route to handle post petitions to accessing a room
    path('send', views.send, name='send'), #route to handle POST request to store data from new messages in the DB
]