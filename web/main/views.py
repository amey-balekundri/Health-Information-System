from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from patient.models import Patient
from doctor.models import Doctor
from main.models import User
from main.forms import ContactUsForm
from main.models import Contact
# Create your views here.

def home(request):
    totalpatients=len(Patient.objects.all())
    totaldoctors=len(Doctor.objects.all())
    return render(request, 'main/home.html',{'totalpatients':totalpatients,'totaldoctors':totaldoctors})

def register(request):
    return render(request,'main/register.html')

def about_us(request):
    return render(request,'main/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            contact.save()
            return redirect ('contact_us')
    else:
        contact_form = ContactUsForm()
    return render(request,'main/contact_us.html',{'contact_form': contact_form})


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            user_type=User.user_type(user)
            if user is not None :
                login(request,user)
                if user_type=='patient':
                    
                    return redirect('patient_dashboard')
                if user_type=='doctor':
                    
                    return redirect('doctor_dashboard')
            else:
                messages.error(request,"Invalid Email or Password")
        else:
                messages.error(request,"Invalid Email or Password")
    return render(request, 'main/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return render(request,'main/logout.html')

def dashboard_redirect(request):
    user_type=User.user_type(request.user)
    if user_type=='patient':
        return redirect('patient_dashboard')
    if user_type=='doctor':
        return redirect('doctor_dashboard')
