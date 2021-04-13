from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
    email=models.EmailField(verbose_name="email",max_length=60,unique=True,primary_key=True)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    objects=MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    
    def user_type(self):
        if self.is_doctor==True:
            return "doctor"
        if self.is_patient==True:
            return "patient"

    def patient_role(self):
        if self.is_patient:
            return "True"
        else:
            return "False"

    def doctor_role(self):
        if self.is_doctor:
            return "True"
        else:
            return "False"


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(default=0)
    message = models.CharField(max_length=300)

	
		
