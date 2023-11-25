
from django.shortcuts import render, get_object_or_404


from django.http import Http404

from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
def product_create_view(request):

  # ------ CON Django FORMS --------------------------------

  initial_data = {
    "title": "Default title"
  } # using initial argument

  obj = Product.objects.get(id=1)# using an instance of an object


  form = ProductForm(request.POST or None, initial=initial_data) # digo el tipo de peticioin a la que respone
  form = ProductForm(request.POST or None, instance=obj)

  if form.is_valid(): #valido el form
    form.save()

  context = {
    "form" : form,
  }


  return render(request, "products/product_create.html", context)


  # ------ SIN Django FORMS --------------------------------

  # POST method routing (store only on post, else render form normally)
  # if (request.method == 'POST'):
  #   title = request.POST.get('title')  # saco query params
  #   print(title)
  #   # Product.objects.create(title=m

  # context = {}
  # return render(request, "products/product_create.html", context)

  # -------- PUre Django FOrms ------

  # form = RawProductForm() # render default form
  # # POST method routing
  # if request.method == 'POST': 
  #   form = RawProductForm(request.POST)

  #   if form.is_valid():
  #     print(form.cleaned_data) #returns data into a dictionary
  #     Product.objects.create(**form.cleaned_data) #paso directamnete los argumentso para crear de una el producot en la DB

  #   else:
  #     print(form.errors)


  # context = {
  #   "form": form
  # }

  # return render(request, "products/product_create.html", context)

def product_detail_view(request, id): #not upper case functinos, and explicit to what it is

  

  # product_obj = get_object_or_404(Product, id=id)

  try:
    product_obj = Product.objects.get(id=id)
  except Product.DoesNotExist:
    raise Http404
  
  # context = {
  #   "title": product_obj.title,
  #   "description": product_obj.description,
  # }


  # mas adecuado por si cambio mi dodel o quiero agregar mas models
  context = {
    "obj" : product_obj,
  }

  
  return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
                        
  #obj = Product.objects.get(id=id) 
  obj =  get_object_or_404(Product, id=id)

  # Post method routing
  if request.method == 'POST':
    #confirmig delete
    obj.delete()

  context = {
    "obj" : obj,
  }

  return render(request, "products/product_delete.html", context)