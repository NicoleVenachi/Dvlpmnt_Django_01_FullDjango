from django.db import models

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True) #it can be b;ank, empty or null ('' este valor pero es reuiered or null)
  price = models.DecimalField(max_digits=10000, decimal_places=2) #
  summary = models.TextField(blank=False, null=False)

  featured = models.BooleanField(default=False) # null or default

  def get_absolute_url(self):
    return f"/products/{self.id}/"
  
