from django.db import models

# Create your models here.
# class Feature:
#   id: int
#   name: str
#   details: str
#   is_true: bool

class Feature(models.Model):
  #id is atumatically created
  name = models.CharField(max_length=40, default='cualsea')
  details = models.CharField(max_length=500, default='asd')
  is_true = models.BooleanField(default=False)


