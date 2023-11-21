from django.shortcuts import render

import json 
import urllib.request # to make fetch request

import os # to read .env variables
# Create your views here.
def index(request):
  
  # POST method routing
  if request.method == 'POST':
    api_key = os.environ.get('API_KEY')
    city = request.POST.get('city') #get the city from the query params

    fetchURL = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(city,api_key)
    res = urllib.request.urlopen(fetchURL).read() #(q)uery (the city)
    

    json_data = json.loads(res) # json -> dict

    # print(json_data)

    data = {
      "country_code": str(json_data["sys"]["country"]),
      "coordinate": str(json_data["coord"]["lon"])+str(json_data["coord"]["lat"]),
      "temp": str(json_data["main"]["temp"] - 273.15) + ' C', #temp is in kelvin
      "pressure": str(json_data["main"]["pressure"]),
      "humidity": str(json_data["main"]["humidity"])
    }

  # GET method routing
  else:
    city = ''
    data = {}

  return render(request, 'index.html', {'city': city, 'data': data})