from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    sprice = models.FloatField(default=None, blank=True, null=True)
    lprice = models.FloatField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"





