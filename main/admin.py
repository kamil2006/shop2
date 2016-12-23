from django.contrib import admin
from main.models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'price')

admin.site.register(Product, ProductAdmin)
