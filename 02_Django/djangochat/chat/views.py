from django.shortcuts import render, redirect

from chat.models import Room, Message

# Create your views here.
def home(request):
  return render(request, 'home.html')

def room(request, room):
  
  return render(request, 'room.html')

def checkview(request):
  #get the room and username from the request
  room = request.POST.get('room_name')
  username = request.POST.get('username')

  #check if the rooms exists (if not create it)
  if not Room.objects.filter(name=room).exists():
    new_room = Room.objects.create(name=room) #creo la room
    new_room.save()
  else:
    pass
  
  return redirect('/'+ room + '/?username=' + username)
  
  
