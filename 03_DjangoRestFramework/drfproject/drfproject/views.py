
#import for rendering template file
from django.shortcuts import render

#importo la API view
from rest_framework.views import APIView

#importo la response object 
from rest_framework.response import Response

class TestView(APIView):

  #get function -> handle get request de la API
  def get(self, request, *args, **kwargs):
    data = {
      "username": "admin",
      "years_active": 10,
    } # data to send back as a response to client
    return Response(data)

