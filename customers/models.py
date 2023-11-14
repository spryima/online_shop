from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    adress = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
