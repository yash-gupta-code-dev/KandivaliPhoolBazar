from tkinter import TRUE
from django.db import models
from django.contrib import admin
import os
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.


class Product(models.Model):

    # Id for fetching Product
    product_id = models.AutoField(primary_key=True)
    # The name of the product (e.g., "Apple iPhone 15")
    name = models.CharField(max_length=255)

    # A URL-friendly version of the name, useful for SEO and clean URLs
    slug = models.SlugField(unique=True, blank=True)

    # A detailed description of the product
    description = models.TextField(blank=False)

   

    # Timestamp of when the product was first created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp of the last update to the product
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign key to a Category model (e.g., "Electronics", "Clothing")
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=False
    )

    # Optional product image, uploaded to the "products/" folder
    image = models.ImageField(upload_to="products/", blank=False, null=True)
    image2 = models.ImageField(upload_to="products/", blank=True, null=True)
    
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






# Delete image file when a Product is deleted
@receiver(post_delete, sender=Product)
def delete_image_on_delete(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)


# Delete old image file when Product is updated with a new image
@receiver(pre_save, sender=Product)
def delete_image_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return  # New instance, nothing to delete

    try:
        old_instance = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return

    old_image = old_instance.image
    new_image = instance.image

    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
