from django.conf.urls import url
from .views import (product_update,product_list,product_detail,product_delete,product_create)
urlpatterns = [
    
	url(r'^$',        product_list, name='list'),
	url(r'^create/$', product_create, name='create'),
	url(r'^(?P<id>\d+)/$', product_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', product_update,name='update'),
	url(r'^(?P<id>\d+)/delete/$', product_delete, name='delete'),

]