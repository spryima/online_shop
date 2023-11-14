from django.urls import path

from cart.views import ShoppingCartListView

urlpatterns = [
    path("", ShoppingCartListView.as_view(), name="shopping-cart-view"),
]

app_name = "cart"
