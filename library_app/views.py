from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.views.generic import TemplateView
from .forms import LibraryLoginForm

# Create your views here.
class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class LibraryPageView(TemplateView):
    template_name = 'library_view.html'

def logout(request):
    """ user logout """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out of the Library. Come again soon!')
    return(redirect(reverse('home')))

def login(request):
    """ login func """
    login_form = LibraryLoginForm()
    return render(request, 'login.html', {'login_form': login_form})