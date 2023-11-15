from django.views.generic import ListView

from .models import CartItem, ShoppingCart


class ShoppingCartListView(ListView):
    model = CartItem
    template_name = "cart/shopping_cart.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        current_user = self.request.user
        # if current_user.is_authenticated:
        cart = ShoppingCart.objects.filter(customer=current_user).first()

        if cart:
            shopping_list = CartItem.objects.filter(cart=cart)
        else:
            shopping_list = []
        # else:

        total_price = 0
        for item in shopping_list:
            item.total_price = item.quantity * item.product.price
            total_price += item.total_price

        context["shopping_list"] = shopping_list
        context["total_price"] = total_price

        return context
