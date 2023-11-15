from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import DetailView

from cart.models import ShoppingCart, CartItem
from customers.models import Customer
from products.models import Product


class CustomerLoginView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        customer = form.get_user()
        login(self.request, customer)

        self.transfer_cart_to_user(customer)

        return super().form_valid(form)

    def transfer_cart_to_user(self, customer):
        cart_session = self.request.session.get("cart", {})
        if cart_session:
            for product_id, quantity in cart_session.items():
                product = Product.objects.get(id=int(product_id))
                cart, _ = ShoppingCart.objects.get_or_create(customer=customer)
                cart_item, created = CartItem.objects.get_or_create(
                    cart=cart, product=product
                )
                if created:
                    cart_item.quantity = quantity
                else:
                    cart_item.quantity += quantity
                cart_item.save()

            self.request.session["cart"] = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
