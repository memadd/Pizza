from django.db import models

# Create your models here.
class Order(models.Model):
    food = models.CharField(max_length=50)
    sprice = models.FloatField(default=None, blank=True, null=True)
    lprice = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.food}  small:{self.sprice}  large:{self.lprice}"

class Toppings(models.Model):
    topp = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.topp}"

#class Cart(models.Model):

