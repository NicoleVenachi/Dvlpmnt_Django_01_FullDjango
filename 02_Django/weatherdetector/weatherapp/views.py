from django.shortcuts import render

import json 
import urllib.request # to make fetch request

import os # to read .env variables
# Create your views here.
def index(request):
  api_key = os.environ.get('API_KEY')
  print(api_key)
  # POST method routing
  if request.method == 'POST':
    city = request.POST.get('city') #get the city from the query params
    # res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=%s&appid=' % city).read() #(q)uery (the city)
    # print(city)

    # json_data = json.loads(res) # json -> dict

    # print(json_data)

    # data = {
    #   "country_code": str(json_data["sys"]["country"])
    # }

  # GET method routing
  else:
    pass
  return render(request, 'index.html', {'city': city})