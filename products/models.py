from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def add_category(self):
        pass

    def remove_category(self):
        pass

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categiries"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def add_product(self):
        pass

    def update_product(self):
        pass

    def remove_product(self):
        pass
