from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from cart.models import ShoppingCart
from .models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product


class AddToCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, _ = ShoppingCart.objects.get_or_create(user=request.user)

        cart.add_product(product)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


class RemoveFromCartView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart = ShoppingCart.objects.get(customer=request.user)

        cart.remove_product(product)

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
