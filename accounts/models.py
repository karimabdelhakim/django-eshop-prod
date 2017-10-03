from __future__ import unicode_literals
from django.conf import settings
from django.db import models


# Create your models here.
def genders():
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    return GENDER_CHOICES
    
class Profile(models.Model):
    customer = models.OneToOneField(settings.AUTH_USER_MODEL,limit_choices_to={'is_staff': False}, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=genders())
    birthdate = models.DateField()
    creditCard = models.CharField(max_length=14)

    def __unicode__(self):
        return self.customer.username
    
    