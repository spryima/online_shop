from cart.models import ShoppingCart, CartItem


def cart_item_count(request):
    if request.user.is_authenticated:
        cart, _ = ShoppingCart.objects.get_or_create(customer=request.user)
        count = sum([item.quantity for item in CartItem.objects.filter(cart=cart)])
    else:
        cart_session = request.session.get("cart", {})
        count = sum(cart_session.values())
    return {"cart_item_count": count}
