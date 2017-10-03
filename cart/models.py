from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from products.models import Product
# from reviews.models import Review

# Create your models here.

class Cart(models.Model):
	customer = models.OneToOneField(settings.AUTH_USER_MODEL,limit_choices_to={'is_staff': False}, on_delete=models.CASCADE)
	
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	


	def __unicode__(self):
		return self.customer.username

	def get_absolute_url(self):
		return reverse("cart:list")	

	# def get_delete_url(self):
	# 	return reverse("cart:delete", kwargs={"id":self.id})			


@receiver(post_save, sender=User)
def save_customer(sender, instance, created, **kwargs):
    user = instance
    if created and not user.is_staff:#if user is registered(not logged in) and not staff
	    Cart.objects.create(customer=user)
    

#---------------------------------------------------------------------------
class CartProduct(models.Model):
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveSmallIntegerField(default=1)
	price = models.FloatField()

	

	def __unicode__(self):
		return self.product.name



	def save(self):
		qs = CartProduct.objects.filter(cart=self.cart,product=self.product)
		if not qs.exists():
		    super(CartProduct, self).save()
		else:
		   return 

