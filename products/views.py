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
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if request.user.is_authenticated:
            cart, _ = ShoppingCart.objects.get_or_create(customer=request.user)
            cart.add_product(product)
        else:
            if product.quantity > 0:
                cart = request.session.get("cart", {})
                cart[str(pk)] = cart.get(str(pk), 0) + 1
                request.session["cart"] = cart
                product.quantity -= 1
                product.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


class RemoveFromCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if request.user.is_authenticated:
            cart = ShoppingCart.objects.get(customer=request.user)
            cart.remove_product(product)
        else:
            cart = request.session.get("cart", {})
            if str(pk) in cart:
                if cart[str(pk)] > 1:
                    cart[str(pk)] -= 1
                else:
                    del cart[str(pk)]
                request.session["cart"] = cart
                product.quantity += 1
                product.save()

        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
