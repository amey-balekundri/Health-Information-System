from django import forms
from doctor.models import Doctor
from django.forms import ModelForm
from utils import utils
from django.core.validators import RegexValidator
class DoctorRegisterForm(ModelForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Please enter your First Name'})
    last_name = forms.CharField(required=True,error_messages={'required':'Please enter your Last Name'})
    middle_name = forms.CharField(required=True,error_messages={'required':'Please enter your Middle Name'})
    phone_number = forms.IntegerField(required=True,validators=[RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
                    error_messages={'invalid':'Please enter valid Phone Number'})
    aadhaar_no = forms.IntegerField(required=True,validators=[RegexValidator('^[2-9]{1}[0-9]{3}[0-9]{4}[0-9]{4}$')],
                    error_messages={'invalid':'Please enter valid Aadhar Number'})
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True, validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select City'})
    specialization = forms.ChoiceField(choices=utils.json_parser("utils/specialization.json"),required=True,validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select Specialization'})
    class Meta:
        model= Doctor
        fields=("first_name","middle_name","last_name","phone_number","aadhaar_no","city","specialization")

class DoctorUpdateForm(ModelForm):
    first_name = forms.CharField(required=True,error_messages={'required':'Please enter your First Name'})
    last_name = forms.CharField(required=True,error_messages={'required':'Please enter your Last Name'})
    middle_name = forms.CharField(required=True,error_messages={'required':'Please enter your Middle Name'})
    phone_number = forms.IntegerField(required=True,validators=[RegexValidator('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$')],
                    error_messages={'invalid':'Please enter valid Phone Number'})
    city = forms.ChoiceField(choices=utils.json_parser("utils/city.json"),required=True, validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select City'})
    specialization = forms.ChoiceField(choices=utils.json_parser("utils/specialization.json"),required=True,validators=[RegexValidator('^(?!\s*$).+')],
                    error_messages={'invalid':'Please select Specialization'})
    class Meta:
        model= Doctor
        fields=("first_name","middle_name","last_name","phone_number","city","specialization","image")