from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'

class TestPageView(TemplateView):
    template_name = 'test.html'

class AgainPageView(TemplateView):
    template_name = 'again.html'