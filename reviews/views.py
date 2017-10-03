from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
# Create your views here.

@login_required#(login_url='/login/')#we added a variable called LOGIN_URL = "/login/" in settings
def review_delete(request,id):

	obj = get_object_or_404(Review,id=id)
	parent_obj_url = obj.product.get_absolute_url()	
	
	if obj.user != request.user:
		messages.success(request,"you do not have permission to this action")
		# response = HttpResponse("you do not have permission to do this")
		# response.status_code = 403
		# return response
		return HttpResponseRedirect(parent_obj_url)

	if request.method == "POST":
		obj.delete()
		messages.success(request,"comment has been deleted")
		return HttpResponseRedirect(parent_obj_url)
	context={"object":obj,"parent":parent_obj_url}
	return render(request,"confirm_delete.html",context)