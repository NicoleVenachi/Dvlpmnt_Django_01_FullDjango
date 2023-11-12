
from rest_framework import serializers #import los frealizers
from .models import Student # importo el modeloa usar

class StudentSerializer(serializers.ModelSerializer): #class del modelo
  class Meta: #class meta specifying/linking the model and the serialize
    model = Student #the model
    fields = (
      'name', 
      'age', 
      'description', 
      'date_enrolled'
    ) #the fields aa usar ene l serializer.


    