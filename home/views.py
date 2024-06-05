from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        # configs = Home.objects.filter()
        context = super().get_context_data(**kwargs)

        # for config in configs:
        #     context[config.key] = config.value
        return context