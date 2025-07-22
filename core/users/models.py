from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=255, unique=True)  # Bria.ai API key
    usage_quota = models.PositiveIntegerField(default=100)  # Generation Quota
    last_login_ip = models.GenericIPAddressField(blank=True, null=True, default='0.0.0.0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['api_key'])]  # API Key Quick Lookup