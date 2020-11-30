from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from patient.models import Patient
from django.forms import ModelForm

class PatientRegisterForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    aadhaar_no=forms.IntegerField(required=True)
    class Meta:
        model= Patient
        fields=('first_name','middle_name','last_name','phone_number','aadhaar_no')
