from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_bytes

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account '
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
            message = "Hello {0},\n {1}".format(user.first_name + " " + user.last_name, activation_link)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:        
        form = UserRegisterForm()
    return render(request, 'signup.html',{'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if request.user.is_authenticated:
        return redirect('/')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}!')
        return render(request,'home/home.html')
    else:        
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = User.objects.get(email__iexact=email)
    #     if not user:
    #         return HttpResponse("user not exist")
    #     if user and user.check_password(password):
    #         if user:
    #             if user.is_active:
    #                 login(request, user)
    #                 next = request.POST.get('next', '/')
    #                 return HttpResponseRedirect(next)
    #             else:
    #                 return HttpResponse("Your account was inactive.")
    #         else:
    #             print("Someone tried to login and failed.")
    #             print("They used username: {} and password: {}".format(email, password))
    #             return HttpResponse("Invalid login details given")
    # else:
    #     return render(request, 'accounts/login.html', {})
