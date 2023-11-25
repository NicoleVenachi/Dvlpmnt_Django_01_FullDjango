
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
  title = forms.CharField(
    label = 'whichever', 
    max_length=100, 
    widget= forms.TextInput(
      attrs = {
        "placeholder": "Your title" 
      }
    )
 )
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(
      attrs= { 
        "class": "new-class-name 2nd-class", #css class
        "id": "id-for-textarea",
        "rows": 20,
        "cols": 80

      }
    )
  )
  price = forms.DecimalField(max_digits=1000, initial=200.00)

