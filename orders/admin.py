from django.contrib import admin
from .models import Order,OrderProduct
# Register your models here.
#admin.site.register(CartProduct)

class OrderProductModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","order_id"]


	class Meta:
		model = OrderProduct

admin.site.register(OrderProduct, OrderProductModelAdmin)




class OrderModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp"]


	class Meta:
		model = Order

admin.site.register(Order, OrderModelAdmin)