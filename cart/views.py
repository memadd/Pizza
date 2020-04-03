from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404


from orders.models import Order

from shopping_cart.extras import generate_order_id, transact, generate_client_token
from shopping_cart.models import OrderItem, Order, Transaction

import datetime
import stripe

@login_required
def add_to_cart(request,pk):
    product = Order.objects.get(id=pk)