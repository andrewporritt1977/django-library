import stripe
from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from library_books.models import Book
from .forms import LibraryLoginForm, UserSignupForm

# Create your views here.
class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def logout(request):
    """ user logout """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out of the Library. Come again soon!')
    return(redirect(reverse('home')))

def login(request):
    """ login func """
    if request.user.is_authenticated:
        return redirect(reverse('books'))

    if request.method == "POST":
        login_form = LibraryLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged into the Library")
                return redirect(reverse('books'))
            else: 
                login_form.add_error(None, "Sorry, some of your details are incorrect. Please try again")

    else:
        login_form = LibraryLoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse('books'))
    
    if request.method == "POST":
        signup_form = UserSignupForm(request.POST)
        
        if signup_form.is_valid():
            signup_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered with the Library")
                """return redirect(reverse('home'))"""
            else :
                messages.error(request, "Apologies, unable to sign up at this time")
    else:
        signup_form = UserSignupForm()
    return render(request, 'signup.html', {
        "signup_form" : signup_form})

def user_card(request):
    """ view user'slibrary card """
    user = request.user.username
    books = Book.objects.all().order_by("title").filter(checked_by__icontains=user)
    return render(request, 'card.html', {"books" : books})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def pay(request): 
    if request.method == 'POST':
        pay = stripe.Charge.create(
            amount=500,
            currency='gbp',
            description='Django Library Charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'pay.html')

def password_reset_done(request):
    return(render(request, 'password_reset_done.html'))

def password_reset_complete(request):
    return(render(request, 'password_reset_complete.html'))

