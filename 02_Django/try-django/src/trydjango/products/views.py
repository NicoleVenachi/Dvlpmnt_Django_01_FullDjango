from django.shortcuts import render

from .models import Product


# Create your views here.
def product_detail_view(request): #not upper case functinos, and explicit to what it is

  product_obj = Product.objects.get(id=1)

  # context = {
  #   "title": product_obj.title,
  #   "description": product_obj.description,
  # }

  # mas adecuado por si cambio mi dodel o quiero agregar mas models
  context = {
    "obj" : product_obj,
  }
  return render(request, "product/detail.html", context)