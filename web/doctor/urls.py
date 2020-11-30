
from django.urls import path
from doctor import views


urlpatterns = [
    path('register/',views.create_doctor,name='doctor_register'),
    path('dashboard/',views.dashboard,name='doctor_dashboard'),
    path('view_patients/',views.view_patients,name='doctor_view_patients'),
    path('patient_reports/',views.patient_reports,name='doctor_patient_report'),
    path('patient_reports/show/',views.show_reports,name='show_reports'),
    path('profile/',views.doctor_profile,name='doctor_profile'),
]