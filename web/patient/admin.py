from django.contrib import admin

# Register your models here.
from patient.models import Patient
admin.site.register(Patient)