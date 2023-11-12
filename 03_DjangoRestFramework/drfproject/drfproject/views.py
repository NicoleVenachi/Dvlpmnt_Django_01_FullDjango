
#import for rendering template file
from django.shortcuts import render

#importo la API view
from rest_framework.views import APIView

#importo la response object 
from rest_framework.response import Response

# de rest también importo el status 
from rest_framework import status


# seriaizer y model (ojo que models y serializer los definí en la app)
from drfapp.serializers import StudentSerializer
from drfapp.models import Student


class TestView(APIView):

  #get function -> handle get request de la API and serializing the data going out
  def get(self, request, *args, **kwargs):
    # Espeficciamos un query set (data a traer)
    qs = Student.objects.all()
    print(qs)
    
    serializer = StudentSerializer(qs, many = True) # creo serializer, para pasar de data en DB a JSON, many = True porque traemos varios registros

    
    return Response(serializer.data) # data to send back as a response to client

  #get method routing (receive data in a form like)
  def post(self, request, *args, **kwargs):

    serializer = StudentSerializer(data=request.data)
    #creamos serializer con la data envida en el post request

    if serializer.is_valid(): #valido si la data tiene la estructura del modelo
      serializer.save() #almaceno la data del json en la DB
      return Response(serializer.data, status=status.HTTP_201_CREATED) #respondo con la data almacenada en la DB
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # en caso que estructura no se sigua, le digoal cliente ue envió mal la data
  
