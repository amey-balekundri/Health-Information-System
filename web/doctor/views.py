from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from doctor.forms import DoctorRegisterForm
from main.forms import UserRegisterForm
from doctor.models import Doctor
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from blockchain import blockchain
from blockchain import contracts
import datetime
from dateutil import tz
from main.models import User
# Create your views here.



def create_doctor(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        doctor_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            address,key=blockchain.create_account()
            txn_hash=blockchain.send_ether(address)
            user = user_form.save(commit=False)
            user.is_doctor=True
            doctor =doctor_form.save(commit=False)
            doctor.email = user
            doctor.address=address
            doctor.privatekey=key
            user.save()
            doctor.save()
            blockchain.is_mined(txn_hash)
            doctor_account=blockchain.load_account(key)
            tx=contracts.addDoctor(doctor_account,doctor.aadhaar_no)
            blockchain.is_mined(tx)
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

def doctor_required(function):
    def decorator(request,*args,**kwargs):
        doctor=User.doctor_role(request.user)
        if doctor=='True':
            return function(request,*args,**kwargs)
        else:
            return redirect('dashboard_redirect')
    return decorator

@login_required
@doctor_required
def dashboard(request):
    doctor=Doctor.objects.filter(email=request.user).values()[0]
    doctor_account=blockchain.load_account(doctor['privatekey'])
    doctorInfo=contracts.doctorInfo(doctor_account)
    patient_access=len(doctorInfo[1])
    return render(request, 'doctor/dashboard.html',{'patient_access':patient_access})

@login_required
@doctor_required
def view_patients(request):
    doctor=Doctor.objects.filter(email=request.user).values()[0]
    doctor_account=blockchain.load_account(doctor['privatekey'])
    doctorInfo=contracts.doctorInfo(doctor_account)
    patients=[]
    for i in doctorInfo[1]:
        patients.append(Patient.objects.filter(address=i).values()[0])
    return render(request,'doctor/view_patients.html',{'patients':patients})
        
@login_required
@doctor_required
def patient_reports(request):
    doctor=Doctor.objects.filter(email=request.user).values()[0]
    doctor_account=blockchain.load_account(doctor['privatekey'])
    doctorInfo=contracts.doctorInfo(doctor_account)
    patients=[]
    report=[]
    for i in doctorInfo[1]:
        patients.append(Patient.objects.filter(address=i).values()[0])
    return render(request,'doctor/patient_reports.html',{'patients':patients,'report':report})

@login_required
@doctor_required
def show_reports(request):
    patient=Patient.objects.filter(email=request.POST['patient']).values()[0]
    doctor=Doctor.objects.filter(email=request.user).values()[0]
    doctor_account=blockchain.load_account(doctor['privatekey'])
    doctorInfo=contracts.doctorInfo(doctor_account)
    report=contracts.viewPatientReport(patient['address'],doctor_account)
    patients=[]
    val=patient['email_id']
    for i in doctorInfo[1]:
        patients.append(Patient.objects.filter(address=i).values()[0])
    for i in range(len(report)):
        report[i]=list(report[i])
        report[i][0]=(datetime.datetime.fromtimestamp(int(report[i][0]), tz.gettz('Asia/Kolkata')).strftime('%d/%m/%Y %I:%M %p'))
    return render(request,'doctor/patient_reports.html',{'patients':patients,'report':report,'val':val})

@login_required
@doctor_required
def doctor_profile(request):
    doctor=Doctor.objects.filter(email=request.user).values()[0]
    return render(request,'doctor/profile.html',{'doctor':doctor})



