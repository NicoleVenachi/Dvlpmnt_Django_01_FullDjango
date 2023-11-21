from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model): # model for the channel - room
  # id created by default
  name = models.CharField(max_length=100)
  
class Message(models.Model): # model for store the messages
  value = models.CharField(max_length=1000000) # message value
  date = models.DateField(default=datetime.now, blank=True)
  user = models.CharField(max_length=1000) #podria hacer un fkey de user, igual con la room
  room = models.CharField(max_length=100)
