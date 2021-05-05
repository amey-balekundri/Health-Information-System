from django.contrib import admin

# Register your models here.
from main.models import User,Contact

admin.site.register(User)
admin.site.register(Contact)
