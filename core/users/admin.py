from django.contrib import admin

# core app imports
from .models import CustomUser

# Register your models here.

admin.site.register(CustomUser)