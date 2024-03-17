from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail

# from the project
from .models import Payment
from . import forms


def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        payment_form = forms.PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            context = {
                'payment': payment,
                'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY,
            }
            return render(request, 'payments/make_payment.html', context)
    else:
        payment_form = forms.PaymentForm()
        context = {
            'payment_form': payment_form,
        }

    return render(request, 'payments/initiate_payment.html', context)

def verify_payment(request: HttpRequest, ref: str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()

    if verified:
        # Payment successful
        send_payment_success_email(payment)
        messages.success(request, 'Payment was successful')
    else:
        # Payment failed
        send_payment_failure_email(payment)
        messages.error(request, 'Payment was not successful')

    return redirect('advert:initiate_payment')

def send_payment_success_email(payment):
    subject = 'Your advertisement is live'
    message = render_to_string('payments/payment_success_email.html', {'payment': payment})
    recipient_email = payment.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

def send_payment_failure_email(payment):
    subject = 'Advertisement Payment Rejected'
    message = render_to_string('payments/payment_failure_email.html', {'payment': payment})
    recipient_email = payment.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

    