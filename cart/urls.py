from django.conf.urls import url
from .views import add_to_cart,cart_list,item_delete
urlpatterns = [
    
	url(r'^$',        cart_list, name='list'),
	url(r'^add/$', add_to_cart, name='add'),
	# url(r'^(?P<id>\d+)/$', product_detail, name='detail'),
	# url(r'^(?P<id>\d+)/edit/$', product_update,name='update'),
	url(r'^item/(?P<id>\d+)/delete/$', item_delete, name='delete-item'),

]