
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):


  # OVERWRITTING default fieds.
  title = forms.CharField(
    label = 'whichever', 
    max_length=100, 
    widget= forms.TextInput(
      attrs = {
        "placeholder": "Your title" 
      }
    )
 )
  email = forms.EmailField()

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


  class Meta:
    model = Product
    fields = {
      "title",
      "description",
      "price",
      # "email"
    }

  # ***** CUSTOMIZED FORMS VALIDATIONS ******

  def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if not "CFE" in title: # valido si el title contiene algo
      raise forms.ValidationError('This is not a valid title')
    
    return title
  

  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get("email")
    if not email.endswith("edu"): # valido si el email contiene algo
      raise forms.ValidationError('This is not a valid email')
    
    return email
  

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

