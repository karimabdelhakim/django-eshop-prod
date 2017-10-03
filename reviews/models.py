from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
# Create your models here.

class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)	
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	content = models.TextField(blank=True)
	rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	class Meta:
		ordering = ['-timestamp']

	def __unicode__(self):
		return str(self.product.name)

	def get_delete_url(self):
		return reverse("comments:delete",kwargs={"id":self.id})		


	