from django import forms
from .models import CartProduct

class CartForm(forms.ModelForm):
	
	class Meta:
		model = CartProduct
		fields = ["quantity"]