
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = {
      "title",
      "description",
      "price",
    }

class RawProductForm(forms.Form):

  #field declaration para validation
  title = forms.CharField(max_length=100)
  description = forms.CharField(max_length=10000)
  price = forms.DecimalField(max_digits=1000)

  