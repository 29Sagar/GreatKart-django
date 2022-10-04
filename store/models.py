from django.urls import reverse
from enum import unique
from tokenize import blank_re
from django.db import models
from traitlets import default

from category.models import Category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    description = models.TextField(max_length =250, blank = True)
    price = models.IntegerField()
    images = models.FileField(upload_to = 'photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now = True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self) -> str:
        return self.product_name