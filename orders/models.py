from django.db import models

from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    items = models.ManyToManyField(Product, through='OrderItem', related_name='order_items')

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name} {self.customer.last_name}"

    class Meta:
        ordering = ["-date"]

    def place_order(self):
        pass

    def cancel_order(self):
        pass

    def update_order(self):
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
