from django.contrib import admin

from .models import Product #add the model to the admin panel
# Register your models here.

admin.site.register(Product)
