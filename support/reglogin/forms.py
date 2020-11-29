from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100,required=True,help_text='Required')
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',
                                message="Phone number must match egyptian format")
    phone = forms.CharField(validators=[phone_regex], max_length=11, min_length=11, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name','last_name','phone', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(max_length=50,widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
