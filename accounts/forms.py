from django import forms
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


#for customer registeration
class UserForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("this email has already been registered")
		return email  


class ProfileForm(forms.ModelForm):
	birthdate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
	class Meta:
		model = Profile
		fields = ['address','phone','creditCard','gender','birthdate']


#for customer and staff login
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	# called when UserLoginForm() is called in the view.
	# if there are ValidationError here or somewhere built-in in the 
	# form class then form.is_valid() in the view will be False. 
	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:#check user entered username and pass not one of them only
			user_qs = User.objects.filter(username=username)
			if user_qs.count()==1:
				user = user_qs.first()
			else: user = None
			print user
			if not user:
				raise forms.ValidationError("this user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:#active user means that he is not banned
				raise forms.ValidationError("this user is no longer active")		
		return super(UserLoginForm, self).clean(*args,**kwargs)#return whatever the function already returns by default

#staff registeration form
class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email2 = forms.EmailField(label='Confirm Email')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','email2','password']
	
	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError("Emails must match")
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("this email has already been registered")
		return email
