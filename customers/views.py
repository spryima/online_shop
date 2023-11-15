from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import DetailView

from customers.models import Customer


class CustomerLoginView(LoginView):
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer

