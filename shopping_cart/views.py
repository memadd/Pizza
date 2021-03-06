from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import OrderItem, Order
from orders.models import Food
from .extras import generate_order_id
from django.contrib import messages

# Create your views here.
def get_user_pending_order(request):
    # get order for the correct user
    order = Order.objects.filter(owner=request.user, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0


@login_required()
def add_to_cart(request, pk):
    p = request.POST.getlist('price')
    price = float(p[0])
    
    product = Food.objects.get(id=pk)
    order_item, status = OrderItem.objects.get_or_create(product=product, price=price)
    # create order associated with the user
    name = request.user
    user_order, status = Order.objects.get_or_create(owner=name, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('orders:index'))

@login_required()
def delete_from_cart(request, pk):
    item_to_delete = OrderItem.objects.filter(id=pk)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('cart:order_summary'))

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'shopping_cart/order_summary.html', context)    