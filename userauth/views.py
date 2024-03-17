# default django imports
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

# send email imports
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# imports from userauth app
from userauth.forms import UserRegisterForm

# third party imports
from django.contrib import messages

# from the project
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            
            # Send email to the new_user
            subject = 'Welcome to Our ProLink!!'
            html_message = render_to_string('userauth/registration_email.html', {'username': username})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data.get('email')
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
            
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('core:home')
    else:
        form = UserRegisterForm()
    return render(request, 'userauth/register.html', {'form': form})

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            # Redirect to the previous page or 'core:index'
            return redirect(request.GET.get('next', 'core:home'))
        else:
            messages.warning(request, 'Invalid email or password')
    return render(request, 'userauth/login.html')

@login_required
def profile_view(request):
    return render(request, 'userauth/profile.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('core:home')

