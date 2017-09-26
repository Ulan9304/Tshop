# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from .forms import SubscriberForm

from products.models import Product

# Create your views here.

def landing(request):
	name = "Coding Mevded"
	currentdate= timezone.now().date()
	form = SubscriberForm(request.POST or None)

	if request.method == "POST" and form.is_valid():
		print (request.POST)
		# print (form.cleaned_data)
		data = form.cleaned_data
		# # print (form.cleaned_data["name"])
		print (data["name"])
		form = form.save()

	return render(request, 'landing/landing.html', locals())


def home(request):
	products = Product.objects.filter(is_active=True)
	context = {
		'products':products
	}

	return render(request, 'landing/home.html', context)
