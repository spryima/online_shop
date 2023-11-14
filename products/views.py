from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 5


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"



# class AddToCartListView(ListView):
#     def post(self, request, product_id):


