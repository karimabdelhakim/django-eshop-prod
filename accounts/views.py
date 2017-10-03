from django.shortcuts import render,redirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from .forms import UserForm,ProfileForm,UserLoginForm,UserRegisterForm
# Create your views here.

User = get_user_model()

#for customer registeration
def register_view(request):
	title = "Customer Register"
	user_form = UserForm(request.POST or None)
	profile_form = ProfileForm(request.POST or None)
	if user_form.is_valid() and profile_form.is_valid():
		user = user_form.save(commit=False)
		password = user_form.cleaned_data.get("password")
		user.set_password(password)
		user.save()#user is registered
		profile = profile_form.save(commit=False)
		profile.customer = user
		profile_form.save()
		new_user = authenticate(username=user.username,password=password)
		login(request, new_user)
		print request.user.is_authenticated()
		return redirect("/")
	context = {"user_form":user_form,"profile_form":profile_form,"title":title}	
	return render(request,"customer_form.html",context) 

#for customer and staff login
def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request, user)
		print request.user.is_authenticated()
		return redirect("/")
		
	return render(request,"login_form.html",{"form":form,"title":title})

#for all
def logout_view(request):
	logout(request)
	return redirect("/")

#staff registeration view	
def register_staff(request):
	title = "Staff Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.is_staff =True
		user.save()#user is registered
		new_user = authenticate(username=user.username,password=password)
		login(request, new_user)
		print request.user.is_authenticated()
		return redirect("/")

	return render(request,"staff_form.html",{"form":form,"title":title})









