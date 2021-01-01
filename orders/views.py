from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.views import generic
from django.views.generic import View

from .models import Food
from . choices import toppings


def index(request):
    context = {
        "pizza": Food.objects.all()[:2],
        "subs": Food.objects.all()[2:16],
        "pasta": Food.objects.all()[16:19],
        "salads": Food.objects.all()[19:23],
        "plates": Food.objects.all()[23:30],
        "toppings": toppings

    }
    return render(request, "orders/index.html", context)

