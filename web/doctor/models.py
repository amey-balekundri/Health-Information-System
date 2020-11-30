from django.db import models
from main.models import User
from PIL import Image
# Create your models here.
class Doctor(models.Model):
    email = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number = models.IntegerField(default=0)
    aadhaar_no=models.IntegerField(default=0)
    address=models.CharField(max_length=50)
    privatekey=models.JSONField(default=dict)
    image=models.ImageField(default='doctor.png',upload_to='profile_pics')