# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *



class ProductImageInline (admin.TabularInline):
	model = ProductImage
	extra = 0

# class ProductImageInline (admin.TabularInline)
class ProductAdmin (admin.ModelAdmin):
	# list_display = ["name","email"]
	list_display = [field.name for field in Product._meta.fields]
	inlines = [ProductImageInline]

	class Meta:
		model = Product


# # Register your models here.

admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
	# list_display = ["name","email"]
	list_display = [field.name for field in ProductImage._meta.fields]

	class Meta:
		model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)

# #         Register your models here.
