from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .utils import send_email_util
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def BaseHTML(request):
    return render(request, "base.html")


def HomePageView(request):
    return render(request, "homepage.html")


class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def ProductPage(request):
    return render(request, "product.html")


def product_detail(request, product_id):
    # Get the product or return 404 if not found
    product = get_object_or_404(Product, product_id=product_id)

    # Check if the request is an AJAX request (for template loading)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        # Return just the product detail template
        return render(request, "product_view.html", {"product": product})

    # Regular request - return full page
    return render(request, "product_view.html", {"product": product})



@csrf_exempt  # Optional if using CSRF token in JS
def send_email(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject="New Contact Form Submission",
            message=full_message,
            from_email="your_email@gmail.com",
            recipient_list=["contact@yourdomain.com"],
            fail_silently=False,
        )
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "invalid request"}, status=400)
