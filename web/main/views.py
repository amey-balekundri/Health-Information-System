from django.shortcuts import render ,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from main.models import User
# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def register(request):
    return render(request,'main/register.html')


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
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'main/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return render(request,'main/logout.html')