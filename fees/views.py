from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from .forms import MakePaymentForm

import stripe


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def fees_pay(request):
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():
        
            try:
                customer = stripe.Charge.create(
                    amount = int(500),
                    Currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, Your card was declined")

            if customer.paid:
                messages.error(request, "Congratulations, you have successfully paid")
                return redirect(reverse('card.html'))

            else:
                messages.error(request, "Unable to take payment at this time")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card")
    else:
        payment_form = MakePaymentForm()

    return render(request, "fees.html", {"payment_form" : payment_form, "publishable" : settings.STRIPE_PUBLISHABLE})