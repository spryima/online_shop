from django.urls import path

from customers.views import CustomerLoginView, CustomerDetailView, CustomerCreateView

urlpatterns = [
    path("<int:pk>/", CustomerDetailView.as_view(), name="profile"),
    path("login/", CustomerLoginView.as_view(), name="login"),
    path("register/", CustomerCreateView.as_view(), name='customer-create'),

]

app_name = "customers"
