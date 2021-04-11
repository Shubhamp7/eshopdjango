from django.db import models
from .category import Category
from .product import Product
import uuid

class Productkeys(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    productkey = models.UUIDField(default=uuid.uuid4,editable=True,unique=True)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    used = models.BooleanField(blank=False,default=False)

    @staticmethod
    def get_productkeys_by_id(ids):
        return Productkeys.objects.filter(id__in=ids)

    @staticmethod
    def get_all_productkeys():
        return Productkeys.objects.all()

    @staticmethod
    def get_all_productkeys_by_productid(product_id):
        if product_id:
            return Productkeys.objects.filter(product=product_id)
        else:
            return Productkeys.get_all_products();

class Usedproductkeys(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    productkey = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    used = models.BooleanField(blank=False, default=False)