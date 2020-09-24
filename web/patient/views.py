from django.shortcuts import render,redirect
from django.contrib import messages
from patient.forms import PatientRegisterForm
from main.forms import UserRegisterForm
from patient.models import Patient
from django.contrib.auth import login, logout,authenticate

def create_patient(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        patient_form = PatientRegisterForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.is_patient=True
            patient = patient_form.save(commit=False)
            patient.email = user
            user.save()
            patient.save()
            login(request,user)

            return redirect('patient_dashboard')
    else:
        user_form = UserRegisterForm()
        patient_form = PatientRegisterForm()
    return render(
        request,
        'patient/register.html',
        {'user_form': user_form, 'patient_form': patient_form}
    )

def dashboard(request):
    user=request.user
    patient=Patient.objects.filter(email=user)
    return render(request, 'patient/dashboard.html',{'patient':patient})