from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("address",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("address",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "address",
                    )
                },
            ),
        )
    )