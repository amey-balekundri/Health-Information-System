
from django.urls import path
from patient import views


urlpatterns = [
    path('register/',views.create_patient,name='patient_register'),
    path('dashboard/',views.dashboard,name='patient_dashboard'),
]