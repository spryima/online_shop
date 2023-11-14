from django.urls import path

from home.views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='main'),
    path('about/', AboutPageView.as_view(), name='about'),
]

app_name = "home"
