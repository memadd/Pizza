from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Orderr
from orders.models import Order
from .extras import generate_order_id
from django.contrib import messages

# Create your views here.
@login_required()
def add_to_cart(request, pk):
    product = Order.objects.get(id=pk)
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    name = ''
    user_order, status = Orderr.objects.get_or_create(owner=name, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('orders:index'))

