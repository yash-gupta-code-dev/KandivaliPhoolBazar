from django.shortcuts import render
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .serializers import ProductSerializer



# Create your views here.

def BaseHTML(request):
    return render(request, 'base.html')


def HomePageView(request):
    return render(request, "homepage.html")


class ProductListView(APIView):
    def get(self,request,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
         serializer = ProductSerializer(data = request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def ProductPage(request):

    return render(request, 'product.html')
