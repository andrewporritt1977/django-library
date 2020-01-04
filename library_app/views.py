from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import LibraryLoginForm

# Create your views here.
class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class LibraryPageView(TemplateView):
    template_name = 'library_view.html'

@login_required
def logout(request):
    """ user logout """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out of the Library. Come again soon!')
    return(redirect(reverse('home')))

def login(request):
    """ login func """
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        login_form = LibraryLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged into the Library")
                return redirect(reverse('home'))
            else: 
                login_form.add_error(None, "Sorry, some of your details are incorrect. Please try again")

    else:
        login_form = LibraryLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def signup(request):
    return render(request, 'signup.html')