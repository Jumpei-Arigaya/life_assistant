from django.db import models


class Industry(models.Model):
    """販売店の種類"""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    """販売店"""

    name = models.CharField(max_length=255)
    shop_branch = models.CharField(max_length=255, null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.shop_branch}"


class Product(models.Model):
    """商品名"""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
