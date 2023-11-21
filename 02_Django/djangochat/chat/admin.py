from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room) # adding the Room model to showcasing them in the admin panel
admin.site.register(Message)