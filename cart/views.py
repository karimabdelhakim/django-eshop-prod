from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q,Sum,F

from .forms import CartForm
from .models import CartProduct,Cart
from products.models import Product
# Create your views here.

@login_required
def add_to_cart(request):
 	
 	form = CartForm(request.POST or None)
 	if form.is_valid() and request.user.is_authenticated() and request.method == 'POST':
 		instance = form.save(commit=False)
 		product_id = int(request.POST.get("product_id"))
 		product = get_object_or_404(Product,id=product_id)
 		cart = Cart.objects.get(customer=request.user)
 		qs = CartProduct.objects.filter(product=product,cart=cart)
 		if not qs.exists():
	 		instance.cart = cart
	 		instance.product = product
	 		price = product.price
			quant = instance.quantity
			total_price = price*quant
			instance.price = total_price
	 		instance.save()
	 		messages.success(request, "item added")
	 		return HttpResponseRedirect(product.get_absolute_url())

 	messages.error(request,"item already in cart")
 	return HttpResponseRedirect("/")

# # @login_required
# # def product_update(request,id):
# # 	if not request.user.is_staff:
# # 		raise Http404
# # 	title = "Update"	
# # 	instance = get_object_or_404(Product,id=id)		
# # 	form = ProductForm(request.POST or None,instance=instance)
# # 	if form.is_valid():
# # 		instance = form.save(commit=False)
# # 		instance.save()
# # 		messages.success(request, "Successfuly Updated")
# # 		return HttpResponseRedirect(instance.get_absolute_url())
	
# # 	context ={"form": form,"title":title}
# # 	return render(request,"product_form.html",context)	
@login_required
def cart_list(request):
	
	cart = Cart.objects.get(customer=request.user)
	queryset = CartProduct.objects.filter(cart=cart)
	total_price = queryset.aggregate(Sum('price'))
	total_price =  total_price['price__sum']
	cart_id = cart.id
	print ('tot',total_price)
	context = {
		"title":"Cart",
		"object_list" :queryset,
		"total_price":total_price,
		"cart_id":cart_id,
	}
	return render(request,"cart_list.html",context)


# # def product_detail(request,id):
# # 	product = get_object_or_404(Product,id=id)
# # 	reviews = Review.objects.all().filter(product=product)	
# # 	form = ReviewForm(request.POST or None)
# # 	if form.is_valid() and request.user.is_authenticated():
# # 		review = form.save(commit=False)
# # 		review.user = request.user 
# # 		review.product = product
# # 		review.save()
# # 		return HttpResponseRedirect(product.get_absolute_url())

# # 	context = {
# # 	"title":product.name,
# # 	"instance":product,
# # 	"review_form":form,
# # 	"reviews":reviews,

# # 	}
# # 	return render(request,"product_detail.html",context)

@login_required
def item_delete(request,id):
	obj = get_object_or_404(CartProduct,id=id)
	
	if (obj.cart.customer != request.user):
		messages.error(request,"you do not have permission to this action")
		return HttpResponseRedirect(obj.get_absolute_url())

	obj.delete()
	messages.success(request,"item has been deleted")
	return HttpResponseRedirect(obj.cart.get_absolute_url())

	
	
	