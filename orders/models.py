from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from products.models import Product
from cart.models import Cart

# from reviews.models import Review

# Create your models here.

class Order(models.Model):
	customer = models.ForeignKey(settings.AUTH_USER_MODEL,limit_choices_to={'is_staff': False}, on_delete=models.CASCADE)
	
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	
	class Meta:
		ordering = ['-timestamp']

	def __unicode__(self):
		return self.customer.username

	def get_absolute_url(self):
		return reverse("order:detail", kwargs={"id":self.id})	
		




#---------------------------------------------------------------------------
class OrderProduct(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product)
	quantity = models.PositiveSmallIntegerField()
	price = models.FloatField()

	

	def __unicode__(self):
		return self.product.name

