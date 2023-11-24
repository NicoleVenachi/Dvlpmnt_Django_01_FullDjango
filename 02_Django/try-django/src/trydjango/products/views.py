from django.shortcuts import render

from .models import Product

from .forms import ProductForm


# Create your views here.
def product_create_view(request):

  form = ProductForm(request.POST or None) # digo el tipo de peticioin a la que respone

  if form.is_valid(): #valido el form
    form.save()

  context = {
    "form" : form,
  }


  return render(request, "products/product_create.html", context)


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

  
  return render(request, "products/product_detail.html", context)