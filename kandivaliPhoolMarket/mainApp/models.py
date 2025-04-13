from django.db import models
from django.contrib import admin
# Create your models here.


class Product(models.Model):
    # The name of the product (e.g., "Apple iPhone 15")
    name = models.CharField(max_length=255)

    # A URL-friendly version of the name, useful for SEO and clean URLs
    slug = models.SlugField(unique=True, blank=True)

    # A detailed description of the product
    description = models.TextField(blank=False)

    # Regular price of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Optional discounted price, if there's a sale or promotion
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=False
    )

    # Current quantity of the product in stock
    stock = models.PositiveIntegerField(blank=False)

    # Whether the product is available for purchase or not
    available = models.BooleanField(default=True)

    # Timestamp of when the product was first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp of the last update to the product
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign key to a Category model (e.g., "Electronics", "Clothing")
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=False
    )

    # Optional product image, uploaded to the "products/" folder
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    def __str__(self):
        # Human-readable name for admin or shell displays
        return self.name



class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True
    )  # Category name (e.g., Roses, Bouquets)
    slug = models.SlugField(unique=True)  # URL-friendly version of the name
    description = models.TextField(blank=True)  # Optional description
    image = models.ImageField(
        upload_to="categories/", blank=True, null=True
    )  # Optional category image
    is_active = models.BooleanField(
        default=True
    )  # Whether this category is currently active
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when last updated

    class Meta:
        verbose_name_plural = "Categories"  # For proper plural display in admin

    def __str__(self):
        return self.name


admin.site.register(Product)
admin.site.register(Category)