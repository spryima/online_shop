from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/index.html"


class AboutPageView(TemplateView):
    template_name = "home/about.html"
