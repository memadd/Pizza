from django.db import models

from orders.models import Order

class OrderItem(models.Model):
    product = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name


class Orderr(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.CharField(max_length=30)
    is_ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        return self.items.all()


    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)


