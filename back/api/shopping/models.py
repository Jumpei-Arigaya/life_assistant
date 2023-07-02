from django.db import models
from django.contrib.auth.models import User
from api.core.models import *


class Receipt(models.Model):
    """領収書"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    shopping = models.ForeignKey(
        "Shopping", on_delete=models.SET_NULL, null=True, blank=True
    )
    receipt_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.receipt_date} - {self.shop.name}"


class ReceiptDetail(models.Model):
    """領収書の明細"""

    receipt = models.ForeignKey(
        Receipt, on_delete=models.CASCADE, related_name="details"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.receipt.receipt_date} - {self.receipt.shop.name} - {self.product}"
        )


class Shopping(models.Model):
    """買い物データ"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_date = models.DateField()
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shopping_date} - {self.user.username} - {self.shop.name}"
