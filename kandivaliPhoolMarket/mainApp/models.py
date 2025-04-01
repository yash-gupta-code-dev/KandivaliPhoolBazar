from pyexpat import model
from django.db import models

# Create your models here.
class ProductModels(models.Model):
    product_name = models.CharField(primary_key=True, max_length = 500),
    product_description = models.TextField(blank = True, null = True),

