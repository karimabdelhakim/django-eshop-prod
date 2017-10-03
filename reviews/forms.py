from django import forms
from .models import Review

def ratings():
    CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        )
    return CHOICES
class ReviewForm(forms.ModelForm):
	rating = forms.ChoiceField(choices=ratings(),widget=forms.RadioSelect)
	content = forms.CharField(required=False,label='',widget=forms.Textarea)
	
	class Meta:
		model = Review
		fields = ['rating','content']