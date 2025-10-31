from django.forms import ModelForm
from .models import ProductImage
# ModelForm helps create a new form class for a given model
# Form classes helps create form objects

class ProductImageForm(ModelForm):
    class Meta:
        model =  ProductImage
        fields = ['img', 'caption']
