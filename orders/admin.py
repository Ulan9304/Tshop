# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *



class ProductInOrderInline (admin.TabularInline):
	model = ProductInOrder
	extra = 0


class StatusAdmin (admin.ModelAdmin):
	# list_display = ["name","email"]
	list_display = [field.name for field in Status._meta.fields]

	class Meta:
		model = Status

# # Register your models here.

admin.site.register(Status, StatusAdmin)

class OrderAdmin (admin.ModelAdmin):
	# list_display = ["name","email"]
	list_display = [field.name for field in Order._meta.fields]
	inlines = [ProductInOrderInline]

	class Meta:
		model = Order

# # Register your models here.

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin (admin.ModelAdmin):
	# list_display = ["name","email"]
	list_display = [field.name for field in ProductInOrder._meta.fields]

	class Meta:
		model = ProductInOrder

# # Register your models here.

admin.site.register(ProductInOrder, ProductInOrderAdmin)


