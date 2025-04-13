from django.shortcuts import render
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import ProductSerializer


# Create your views here.
def HomePageView(request):
    return render(request, "homepage.html")


class ProductListView(ListAPIView):
    """
    Returns a list of all available products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
