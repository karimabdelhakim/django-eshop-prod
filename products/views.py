from django.shortcuts import render

from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q ,Avg,Count

from reviews.forms import ReviewForm
from reviews.models import Review
from .forms import ProductForm
from .models import Product

# Create your views here.
@login_required
def product_create(request):
	if not request.user.is_staff:
		raise Http404	
	title = "Create"
	form = ProductForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.admin = request.user
		instance.save()
		messages.success(request, "Successfuly Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context ={"form": form,"title":title}
	return render(request,"product_form.html",context)

@login_required
def product_update(request,id):
	if not request.user.is_staff:
		raise Http404
	title = "Update"	
	instance = get_object_or_404(Product,id=id)		
	form = ProductForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfuly Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context ={"form": form,"title":title}
	return render(request,"product_form.html",context)	

def product_list(request):
	queryset_list = Product.objects.all()
	query = request.GET.get('q')
	if query:
		queryset_list= queryset_list.filter(
			Q(name__icontains=query) |
			Q(description__icontains=query) |
			Q(seller__icontains=query) |
			Q(category__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 10) # Show 3 posts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"title":"products",
		"object_list" :queryset,
		"page_request_var":page_request_var,
	}
	return render(request,"product_list.html",context)


def product_detail(request,id):
	product = get_object_or_404(Product,id=id)
	reviews = Review.objects.all().filter(product=product)	
	average_rating = reviews.aggregate(Avg('rating'))
	if average_rating['rating__avg']:
		average_rating = int(round(average_rating['rating__avg']))
	else:
		average_rating = 0
	reviews_count = reviews.aggregate(Count('id'))
	reviews_count = reviews_count['id__count']
	
	form = ReviewForm(request.POST or None)
	if form.is_valid() and request.user.is_authenticated():
		review = form.save(commit=False)
		review.user = request.user 
		review.product = product
		review.save()
		return HttpResponseRedirect(product.get_absolute_url())

	context = {
	"title":product.name,
	"instance":product,
	"review_form":form,
	"reviews":reviews,
	"average_rating":average_rating,
	"reviews_count":reviews_count

	}
	return render(request,"product_detail.html",context)

@login_required
def product_delete(request,id):
	obj = get_object_or_404(Product,id=id)
	
	if not request.user.is_staff: #or (obj.admin != request.user)
		messages.success(request,"you do not have permission to this action")
		return HttpResponseRedirect(obj.get_absolute_url())

	if request.method == "POST":
		obj.delete()
		messages.success(request,"Product has been deleted")
		return HttpResponseRedirect("/")

	else:
		messages.error(request,"the request must be POST")
		return HttpResponseRedirect("/")
	
	