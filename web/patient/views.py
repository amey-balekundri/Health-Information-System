from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from patient.forms import PatientRegisterForm,PatientUpdateForm
from main.forms import UserRegisterForm
from patient.models import Patient
from patient.forms import BasicForm
from patient.models import Basic
from doctor.models import Doctor
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from blockchain import blockchain   
from blockchain import contracts
from utils import files
import datetime
from dateutil import tz
from main.models import User
from django.db.models import Q

def create_patient(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        patient_form = PatientRegisterForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            address,key=blockchain.create_account()
            txn_hash=blockchain.send_ether(address)
            user = user_form.save(commit=False)
            user.is_patient=True
            patient = patient_form.save(commit=False)
            patient.email = user
            patient.address=address
            patient.privatekey=key
            user.save()
            patient.save()
            Basic.objects.create(email=user)
            blockchain.is_mined(txn_hash)
            patient_account=blockchain.load_account(key)
            tx=contracts.addPatient(patient_account,patient.aadhaar_no)
            blockchain.is_mined(tx)
            login(request,user)

            return redirect('basic')
    else:
        user_form = UserRegisterForm()
        patient_form = PatientRegisterForm()
    return render(
        request,
        'patient/register.html',
        {'user_form': user_form, 'patient_form': patient_form}
    )


def patient_required(function):
    def decorator(request,*args,**kwargs):
        patient=User.patient_role(request.user)
        if patient=='True':
            return function(request,*args,**kwargs)
        else:
            return redirect('dashboard_redirect')
    return decorator

@login_required
@patient_required
def dashboard(request):
    user=request.user
    patient=Patient.objects.filter(email=user).values()[0]
    basic_data=Basic.objects.filter(email=user).values()[0]
    patient_account=blockchain.load_account(patient['privatekey'])
    patientInfo=contracts.patientInfo(patient_account)
    totalreports=len(patientInfo[1])
    doctor_access=len(patientInfo[2])
    blockchain.check_for_sufficient_balance(patient_account.address)
    return render(request, 'patient/dashboard.html',{'totalreports':totalreports,'doctor_access':doctor_access,'basic_data':basic_data})

@login_required
@patient_required
def view_reports(request):
    user=request.user
    patient=Patient.objects.filter(email=user).values()[0]
    patient_account=blockchain.load_account(patient['privatekey'])
    report=contracts.viewReport(patient_account)
    for i in range(len(report)):
        report[i]=list(report[i])
        report[i][0]=(datetime.datetime.fromtimestamp(int(report[i][0]), tz.gettz('Asia/Kolkata')).strftime('%d/%m/%Y %I:%M %p'))
    return render(request, 'patient/view_report.html',{'report':report})

@login_required
@patient_required
def upload_report(request):
    if request.method == 'POST':
        user=request.user
        report=request.FILES['file']
        patient=Patient.objects.filter(email=user).values()[0]
        patient_account=blockchain.load_account(patient['privatekey'])
        file_hash=files.upload_file(report)
        txn_hash=contracts.addReport(request.POST['file_name'],file_hash,patient_account)
        blockchain.is_mined(txn_hash)
        return redirect('patient_dashboard')
    return render(request,'patient/upload_report.html')

@login_required
@patient_required
def revoke_doctor(request):
    user=request.user
    patient=Patient.objects.filter(email=user).values()[0]
    patient_account=blockchain.load_account(patient['privatekey'])
    patientInfo=contracts.patientInfo(patient_account)
    doctor_address=patientInfo[2]
    doctors=[]
    for i in doctor_address:
        doc=Doctor.objects.filter(address=i).values()[0]
        doctors.append(doc)
    return render(request,'patient/revoke_doctor.html',{'doctors':doctors})

@login_required
@patient_required
def access_doctor(request):
    return render(request,'patient/access_doctor.html')

def search_doctor(request):
    search_value=request.GET.get('doctor')
    if search_value.isdigit():
        doctor=Doctor.objects.filter(Q(aadhaar_no=search_value) | Q(phone_number=search_value)).values()[0]
    else:
        doctor=Doctor.objects.filter(Q(email=search_value)).values()[0]
    return JsonResponse(doctor)


def grant_access(request):
    if request.method == 'POST':
        patient=Patient.objects.filter(email=request.user).values()[0]
        patient_account=blockchain.load_account(patient['privatekey'])
        doctor_address=Doctor.objects.filter(email=request.POST['email_id']).values()[0]['address']
        txn_hash=contracts.grantAccessToDoctor(doctor_address,patient_account)
        blockchain.is_mined(txn_hash)
        return redirect('patient_dashboard')


def revoke_access(request):
    if request.method == "POST":
        patient=Patient.objects.filter(email=request.user).values()[0]
        patient_account=blockchain.load_account(patient['privatekey'])
        doctor_address=Doctor.objects.filter(email=request.POST['email_id']).values()[0]['address']
        txn_hash=contracts.revokeAccess(doctor_address,patient_account)
        blockchain.is_mined(txn_hash)
        return redirect('patient_dashboard')

@login_required
@patient_required
def patient_profile(request):
    patient=Patient.objects.filter(email=request.user).values()[0]
    if request.method == 'POST':
        updateform=PatientUpdateForm(request.POST,request.FILES,instance=request.user.patient)
        if updateform.is_valid():
            form=updateform.save(commit=False)
            form.email=request.user
            form.save()        
            return redirect('patient_profile')
    else:
        updateform=PatientUpdateForm(instance=request.user.patient)
    return render(request,'patient/profile.html',{'patient':patient,'form':updateform})

@login_required
@patient_required
def basic(request):
    if request.method == 'POST':
        basic_form=BasicForm(request.POST)
        form = basic_form.save(commit=False)
        form.email=request.user
        form.save()
        return redirect('patient_dashboard')
    else:
        basic_form=BasicForm(instance=request.user.basic)
    return render(request, 'patient/basic.html',{'basic_form': basic_form})

