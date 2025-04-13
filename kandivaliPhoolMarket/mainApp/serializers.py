from rest_framework import serializers
from .models import Product, Category



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # or list fields like ['id', 'name', 'price', ...]
