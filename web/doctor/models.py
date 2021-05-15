from django.db import models
from main.models import User
from PIL import Image
# Create your models here.
class Doctor(models.Model):
    email = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number = models.PositiveBigIntegerField(default=0,unique=True)
    aadhaar_no=models.PositiveBigIntegerField(default=0,unique=True)
    specialization=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    privatekey=models.JSONField(default=dict)
    image=models.ImageField(default='doctor.png',upload_to='profile_pics')