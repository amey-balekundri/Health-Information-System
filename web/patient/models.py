from django.db import models
from main.models import User
from PIL import Image
# Create your models here.
class Patient(models.Model):
    email = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number = models.IntegerField(default=0)
    aadhaar_no=models.IntegerField(default=0)
    address=models.CharField(max_length=50)
    privatekey=models.JSONField(default=dict)
    image=models.ImageField(default='patient.png',upload_to='profile_pics')

class Basic(models.Model):
    email = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    blood_group = models.CharField(max_length=10)
    allergies = models.CharField(max_length=300)
    operations = models.CharField(max_length=300)
    