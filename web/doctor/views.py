from django.shortcuts import render,redirect
from django.contrib import messages
from doctor.forms import DoctorRegisterForm
from main.forms import UserRegisterForm
from doctor.models import Doctor
from django.contrib.auth import login, logout,authenticate
# Create your views here.



def create_doctor(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        doctor_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.is_doctor=True
            doctor =doctor_form.save(commit=False)
            doctor.email = user
            user.save()
            doctor.save()
            login(request,user)
            
            return redirect('doctor_dashboard')
    else:
        user_form = UserRegisterForm()
        doctor_form = DoctorRegisterForm()
    return render(
        request,
        'doctor/register.html',
        {'user_form': user_form, 'doctor_form':doctor_form}
    )

def dashboard(request):
    user=request.user
    doctor=Doctor.objects.filter(email=user)
    return render(request, 'doctor/dashboard.html',{'doctor':doctor})