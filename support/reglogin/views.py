from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from .models import Users

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account '
            to_email = form.cleaned_data.get('email')
            message = render_to_string('activateuser.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:        
        form = UserRegisterForm()
    return render(request, 'signup.html',{'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64)).decode() 
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.info(request,'Account Activated Successfully')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

def loginform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Users.objects.filter(email=email)
        if not user:
            return HttpResponse("user not exist")
        if user and user.check_password(password):
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('signup')
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                messages.info(request,'Invalid Login Details Given')
    else:
        return render(request, 'login.html', {})

# def loginform(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         userlogin = authenticate(request, email=email, password=password)
#         if userlogin:
#             # if userlogin.is_active:
#             login(request, userlogin)
#             return redirect('signup')
#         else:
#             messages.info(request,'Invalid Login Details Given')

#     return render(request, 'login.html', {})


def logoutform(request):
    logout(request)
    return redirect('login')
    
   