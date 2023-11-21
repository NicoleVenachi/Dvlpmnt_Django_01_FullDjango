from django.shortcuts import render, redirect

from chat.models import Room, Message

from django.http import HttpResponse, JsonResponse #JSON response, par respnder directamente un json


# Create your views here.
def home(request):
  return render(request, 'home.html')

def room(request, room):

  username = request.GET.get('username')

  room_details = Room.objects.get(name=room)
  
  return render(request, 'room.html', {
    "username": username,
    "room": room,
    "room_details": room_details
  })

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
  
  #at the end, route to the room
  return redirect('/'+ room + '/?username=' + username)
  
  
def send(request):
  #get the room, username and message from the request
  room_id = request.POST.get('room_id') # mismo que el name room
  username = request.POST.get('username')
  message = request.POST.get('message')

  #creo objeto y lo almaceno
  new_message = Message.objects.create(value = message, user = username, room = room_id)
  new_message.save()
  
  #at the end, send a http response message 
  return HttpResponse('Message sent successfully')

def getMessages(request, room):

  room_details = Room.objects.get(name=room) #get only one

  roomMessages = Message.objects.filter(room =room_details.id) # get serveral instances

  # retur directly a json reponse
  return JsonResponse({"messages": list(roomMessages.values())} )