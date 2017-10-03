from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q,Sum

from .models import OrderProduct,Order
from products.models import Product
from cart.models import Cart,CartProduct
from accounts.models import Profile
# Create your views here.

@login_required
def make_order(request):
 	
 	
 	if request.user.is_authenticated():
 		order = Order.objects.create(customer=request.user)
 		cart = Cart.objects.get(customer=request.user)
 		cart_qs = CartProduct.objects.filter(cart=cart)
 		if cart_qs.exists():#cart not empty
	 		for cart_item in cart_qs:
	 			OrderProduct.objects.create(order=order,product=cart_item.product,
	 				quantity=cart_item.quantity,price=cart_item.price)
	 		cart_qs.delete()#all user cart items are deleted
	 		if not cart_qs.exists():
		 		messages.success(request, "New order Successfuly added!")
		 		return HttpResponseRedirect(order.get_absolute_url())#url to order detail

		 	messages.error(request,"order failed!")
		 	return HttpResponseRedirect("/")
	messages.error(request,"there are no items to order!")
	return HttpResponseRedirect("/")	 	

@login_required
def order_list(request):
	
	orders_qs = Order.objects.filter(customer=request.user)
	context = {
		"title":"Order history",
		"orders_qs" :orders_qs,
	}
	return render(request,"order_list.html",context)

@login_required
def order_detail(request,id):
	order = get_object_or_404(Order,id=id)
	order_qs = OrderProduct.objects.filter(order=order)
	total_price = order_qs.aggregate(Sum('price'))
	total_price = total_price['price__sum']	
	profile = Profile.objects.get(customer=request.user)
	
	context = {
	"title":"Order details",
	"timestamp":order.timestamp,
	"order_qs":order_qs,
	"total_price":total_price,
	"address":profile.address,
	"phone":profile.phone,
	}
	return render(request,"order_detail.html",context)

	