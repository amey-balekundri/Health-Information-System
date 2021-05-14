from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm
from patient.models import Patient
from patient.models import Basic
from django.forms import ModelForm
from utils import utils
from django.core.validators import RegexValidator

class PatientRegisterForm(ModelForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Please enter your First Name'})
    last_name = forms.CharField(required=True,error_messages={'required':'Please enter your Last Name'})
    middle_name = forms.CharField(required=True,error_messages={'required':'Please enter your Middle Name'})
    phone_number = forms.IntegerField(required=True,validators=[RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
                    error_messages={'invalid':'Please enter valid Phone Number'})
    aadhaar_no=forms.IntegerField(required=True,validators=[RegexValidator('^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$')],
                    error_messages={'invalid':'Please enter valid Aadhar Number'})
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True, validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select City'})
    class Meta:
        model= Patient
        fields=('first_name','middle_name','last_name','phone_number','aadhaar_no','city')

class PatientUpdateForm(ModelForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Please enter your First Name'})
    last_name = forms.CharField(required=True,error_messages={'required':'Please enter your Last Name'})
    middle_name = forms.CharField(required=True,error_messages={'required':'Please enter your Middle Name'})
    phone_number = forms.IntegerField(required=True,validators=[RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
                    error_messages={'invalid':'Please enter valid Phone Number'})
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True, validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select City'})

    class Meta:
        model=Patient
        fields=('first_name','middle_name','last_name','phone_number','city','image')

class BasicForm(ModelForm):
    height = forms.IntegerField(required=True,label="Height (in cm)",
                error_messages={'required':'Please enter your Height'})
    weight = forms.IntegerField(required=True,label="Weight (in kg)",
                error_messages={'required':'Please enter your Weight'})
    blood_group = forms.CharField(required=True,label="Blood Group",
                error_messages={'required':'Please enter your Blood Group'})
    allergies = forms.CharField(required=False,label="Any Specific Allergy")
    operations = forms.CharField(required=False,label="Any Minor/Major Operation")
    class Meta:
        model= Basic
        fields=('height','weight','blood_group','allergies','operations')

class Search(forms.Form):
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True)
    specialization=forms.ChoiceField(choices=utils.json_parser("utils/specialization.json"),required=True)