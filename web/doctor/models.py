from django.db import models
from main.models import User
# Create your models here.
class Doctor(models.Model):
    email = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    