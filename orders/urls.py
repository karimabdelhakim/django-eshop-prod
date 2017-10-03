from django.conf.urls import url
from .views import make_order,order_detail,order_list
urlpatterns = [
    
	url(r'^$',      order_list, name='list'),
	url(r'^(?P<id>\d+)/$', order_detail, name='detail'),
	url(r'^submit/$',      make_order, name='submit'),
]