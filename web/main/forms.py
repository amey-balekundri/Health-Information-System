from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Contact
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class ContactUsForm(ModelForm):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    message = forms.CharField(required=True)
    class Meta:
        model= Contact
        fields=('full_name','email','phone_number','message')