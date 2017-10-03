from django.conf.urls import url
from django.contrib import admin
from .views import review_delete
urlpatterns = [
   
	url(r'^(?P<id>\d+)/delete/$', review_delete, name='delete'),

]