
from django.urls import path
from doctor import views


urlpatterns = [
    path('register/',views.create_doctor,name='doctor_register'),
    path('dashboard/',views.dashboard,name='doctor_dashboard'),

]