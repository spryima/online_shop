from django.urls import path

from customers.views import CustomerLoginView, CustomerDetailView


urlpatterns = [
    path("<int:pk>/", CustomerDetailView.as_view(), name="profile"),
    path("login/", CustomerLoginView.as_view(), name="login"),

]

app_name = "customers"
