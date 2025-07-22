from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class ImageGenerationJob(models.Model):
    STATUS_CHOICES = [
        ('queued', 'In queue'),
        ('processing', 'Processing'),
        ('completed', 'Complete'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="generated_images")
    prompt = models.TextField()  # Original prompt word
    enhanced_prompt = models.TextField(blank=True)  # Enhanced prompt
    parameters = models.JSONField(default=dict)  # Generation parameters (temperature, resolution, etc.)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    image_url = models.URLField(blank=True)  # Image
    bria_response = models.JSONField(blank=True)  # Raw API Response

    class Meta:
        indexes = [
            models.Index(fields=['status']),  # Status query optimization
            models.Index(fields=['user', '-created_at']),  # Quick access to the latest records
        ]


class PromptTemplate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    template = models.TextField()  # Templates with placeholders (such as"{subject} in {style}"）
    version = models.PositiveSmallIntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)



class BriaAPILog(models.Model):
    job = models.OneToOneField(ImageGenerationJob, on_delete=models.CASCADE)
    request_body = models.TextField()
    response_time = models.FloatField()  # API response time (ms)
    error_code = models.CharField(max_length=50, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=4)  # Billing amount