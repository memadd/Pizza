from rest_framework import serializers
from .models import Cart

class CartSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'