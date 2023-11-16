from django.urls import path

from home.views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="main"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
]

app_name = "home"
