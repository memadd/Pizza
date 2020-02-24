from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from django.views import generic
from django.views.generic import View

from .models import Order


def index(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, "orders/index.html", context)

