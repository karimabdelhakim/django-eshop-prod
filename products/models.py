from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
# from reviews.models import Review

# Create your models here.

def default_image():
	return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

class Product(models.Model):
	admin = models.ForeignKey(settings.AUTH_USER_MODEL,limit_choices_to={'is_staff': True},default=1)
	name = models.CharField(max_length=120)
	seller = models.CharField(max_length=120)
	category = models.CharField(max_length=120)
	description = models.TextField()
	price = models.FloatField()
	stock = models.IntegerField(default=1)
	image = models.CharField(max_length=800,blank=True,default=default_image())
	
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)


	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("product:detail", kwargs={"id":self.id})	

	def get_delete_url(self):
		return reverse("product:delete", kwargs={"id":self.id})			
