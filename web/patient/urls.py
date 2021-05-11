
from django.urls import path
from patient import views


urlpatterns = [
    path('register/',views.create_patient,name='patient_register'),
    path('dashboard/',views.dashboard,name='patient_dashboard'),
    path('profile/',views.patient_profile,name='patient_profile'),
    path('basic/',views.basic,name='basic'),

    path('view_reports/',views.view_reports,name='patient_view_reports'),
    path('upload_report/',views.upload_report,name='patient_upload_report'),

    path('access_doctor',views.access_doctor,name='patient_access_doctor'),
    path('access_doctor/search_doctor/',views.search_doctor,name='search_doctor'),
    path('access_doctor/search_doctor2/',views.search_doctor_city_specialization,name='search_doctor2'),
    path('access_doctor/grant_access/',views.grant_access,name='grant_access'),

    path('revoke_doctor',views.revoke_doctor,name='patient_revoke_doctor'),
    path('revoke_doctor/revoke_access/',views.revoke_access,name='revoke_access'),
]
