from django.urls import path

from products.views import (
    ProductListView,
    ProductDetailView,
    AddToCartView,
    RemoveFromCartView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>", ProductDetailView.as_view(), name="product-detail"),
    path("<int:pk>/add/", AddToCartView.as_view(), name="add-to-cart"),
    path("<int:pk>/remove/", RemoveFromCartView.as_view(), name="remove-from-cart"),
]

app_name = "products"
