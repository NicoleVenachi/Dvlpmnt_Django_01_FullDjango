from django.db import models

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True) #it can be b;ank, empty or null ('' or null)
  price = models.DecimalField(max_digits=10000, decimal_places=2) #
  summary = models.TextField()

