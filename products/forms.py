from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = [ "name", "category", "seller","price","stock","image","description"]