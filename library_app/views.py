from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class LibraryPageView(TemplateView):
    template_name = 'library_view.html'

def logout(request):
    """ user logout """
    auth.logout(request)
    return(redirect(reverse('home')))