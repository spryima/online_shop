from django.db import models

from customers.models import Customer
from products.models import Product


class ShoppingCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='shopping_cart')
    items = models.ManyToManyField(Product, through='CartItem', related_name='cart_items')

    def add_product(self, product):
        pass

    def remove_product(self, product):
        pass

    def __str__(self):
        return f"ShoppingCart of {self.customer.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart {self.cart.id}"
