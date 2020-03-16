from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Cart
from orders.models import Order

def view(requset):
    cart = Cart.objects.all()[0]
    context={
        "cart":cart
    }
    template ="cart/view.html"
    return render (requset, template, context)

def update_cart(request, slug):
    cart = Cart.objects.all()[0]
    try:
        order = Order.objects.get(slug=slug)
    except Order.DoesNotExist:
        pass
    except:
        pass
    cart.order_items.add(order)



