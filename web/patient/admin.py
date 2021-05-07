from django.contrib import admin

# Register your models here.
from patient.models import Patient,Basic
admin.site.register(Patient)
admin.site.register(Basic)