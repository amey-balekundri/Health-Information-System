from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Contact
from django.forms import ModelForm
from django.core.validators import RegexValidator

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class ContactUsForm(ModelForm):
    full_name = forms.CharField(required=True,error_messages={'required':'Please enter your Full Name'})
    email = forms.EmailField(required=True,error_messages={'required':'Please enter your Email Id'})
    phone_number = forms.IntegerField(required=True,validators=[RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
                    error_messages={'invalid':'Please enter valid Phone Number'})
    message = forms.CharField(required=True,error_messages={'required':'Please enter your Message'})
    class Meta:
        model= Contact
        fields=('full_name','email','phone_number','message')