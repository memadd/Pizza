from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.views import generic
from django.views.generic import View

from .models import Order, Toppings


def index(request):
    context = {
        "pizza": Order.objects.all()[:2],
        "subs": Order.objects.all()[2:16],
        "pasta": Order.objects.all()[16:19],
        "salads": Order.objects.all()[19:23],
        "plates": Order.objects.all()[23:30],
        "toppings":Toppings.objects.all()

    }
    return render(request, "orders/index.html", context)

