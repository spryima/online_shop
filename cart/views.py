from django.views.generic import ListView

from products.models import Product
from .models import CartItem, ShoppingCart


class ShoppingCartListView(ListView):
    model = CartItem
    template_name = "cart/shopping_cart.html"

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            cart, _ = ShoppingCart.objects.get_or_create(customer=current_user)
            return CartItem.objects.filter(cart=cart)
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shopping_list = self.get_queryset()

        if not self.request.user.is_authenticated:
            cart_session = self.request.session.get("cart", {})
            for product_id, quantity in cart_session.items():
                product = Product.objects.get(id=int(product_id))
                item = CartItem(product=product, quantity=quantity)
                shopping_list.append(item)

        total_price = 0
        for item in shopping_list:
            item.total_price = item.quantity * item.product.price
            total_price += item.total_price

        context["shopping_list"] = shopping_list
        context["total_price"] = total_price

        return context
