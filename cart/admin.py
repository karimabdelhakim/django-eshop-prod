from django.contrib import admin
from .models import Cart,CartProduct
# Register your models here.
admin.site.register(Cart)
#admin.site.register(CartProduct)






class CartProductModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","price"]


	class Meta:
		model = CartProduct

admin.site.register(CartProduct, CartProductModelAdmin)