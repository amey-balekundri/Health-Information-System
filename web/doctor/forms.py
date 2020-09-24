from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from doctor.models import Doctor
from django.forms import ModelForm

class DoctorRegisterForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    class Meta:
        model= Doctor
        fields=('first_name','middle_name','last_name','phone_number')