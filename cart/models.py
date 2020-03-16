from django.db import models
from orders.models import Order
#from django.contrib.auth.models import User

class Cart (models.Model):
    #user = models.ForeignKey(User, default=1)
    order_items = models.ManyToManyField(Order, null=True, blank=True)
    total = models.DecimalField(max_digits=5, decimal_places=2, default=0.00) 
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)

