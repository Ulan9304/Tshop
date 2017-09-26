# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name 

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)



def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
# from django.db.models.signals import post_save

# # Create your models here.
# class Status (models.Model):
# 	name = models.CharField(max_length=24, blank=True, null=True, default=None)
# 	is_active = models.BooleanField(default=True)
# 	created = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	

# 	# exclude = ["self.id, email"]
# 	def __str__(self):
# 		return "Статус %s" % self.name

# 	class Meta:
# 		verbose_name = 'Статус заказа'
# 		verbose_name_plural = 'Статусы заказа'


# class Order (models.Model):
# 	total_price = models.DecimalField(max_digits=10, decimal_places = 2, default=0	) #total price for all products in order
# 	customer_email =models.EmailField(max_length=48, blank=True, null=True, default=None)
# 	customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
# 	customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
# 	customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
# 	comments = models.TextField(blank=True, null=True, default=None)
# 	created = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	status = models.ForeignKey(Status)


# 	# exclude = ["self.id, email"]
# 	def __str__(self):
# 		return "Заказ %s %s" % ( self.id, self.status.name) 

# 	class Meta:
# 		verbose_name = 'Заказ'
# 		verbose_name_plural = 'Заказы'

# 	def save(self, *args, **kwargs):
# 		super(Order, self).save(*args, **kwargs)



# class ProductInOrder (models.Model):
# 	order = models.ForeignKey(Order, blank=True, null=True, default=None)
# 	product = models.ForeignKey(Product, blank=True, null=True, default=None)
# 	nmb = models.IntegerField (default=1)
# 	price_per_item = models.DecimalField(max_digits=10, decimal_places = 2, default=0)
# 	total_price = models.DecimalField(max_digits=10, decimal_places = 2, default=0) #price*nmb
# 	created = models.DateTimeField(auto_now_add=True, auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
# 	is_active = models.BooleanField(default=True)


# 	# exclude = ["self.id, email"] # self.product.name vidaet imya v modeli product v papke Products i pokazyvaet imya producta v ProductInOrder
# 	def __str__(self):
# 		return "%s" % self.product.name

# 	class Meta:
# 		verbose_name = 'Товар в заказе'
# 		verbose_name_plural = 'Товары в заказе'


# 	def save(self, *args, **kwargs):
#        price_per_item = self.product.price
#        self.price_per_item = price_per_item
#        self.total_price = self.nmb * price_per_item

#        super(ProductInOrder, self).save(*args, **kwargs)



# 	def product_in_order_post_save(sender, instance, created, **kwargs):
#     	order = instance.order
#     	all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

# 	    order_total_price = 0
#     	for item in all_products_in_order:
#         	order_total_price += item.total_price

#  	   instance.order.total_price = order_total_price
#     instance.order.save(force_update=True)


# post_save.connect(product_in_order_post_save, sender=ProductInOrder)