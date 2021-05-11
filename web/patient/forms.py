from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from patient.models import Patient
from patient.models import Basic
from django.forms import ModelForm
from utils import utils

class PatientRegisterForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    aadhaar_no=forms.IntegerField(required=True)
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True)
    class Meta:
        model= Patient
        fields=('first_name','middle_name','last_name','phone_number','aadhaar_no','city')

class PatientUpdateForm(ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=True)
    phone_number = forms.IntegerField(required=True)
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True)

    class Meta:
        model=Patient
        fields=('first_name','middle_name','last_name','phone_number','city','image')

class BasicForm(ModelForm):
    height = forms.IntegerField(required=True,label="Height (in cm)")
    weight = forms.IntegerField(required=True,label="Weight (in kg)")
    blood_group = forms.CharField(required=True,label="Blood Group")
    allergies = forms.CharField(required=False,label="Any Specific Allergy")
    operations = forms.CharField(required=False,label="Any Minor/Major Operation")
    class Meta:
        model= Basic
        fields=('height','weight','blood_group','allergies','operations')

class Search(forms.Form):
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True)
    specialization=forms.ChoiceField(choices=utils.json_parser("utils/specialization.json"),required=True)