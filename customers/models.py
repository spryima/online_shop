from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Customer(AbstractUser):
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("customers:profile", kwargs={"pk": self.pk})
