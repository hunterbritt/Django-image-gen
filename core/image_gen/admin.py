from django.contrib import admin

# core app imports
from .models import PromptTemplate, ImageGenerationJob
# Register your models here.

admin.site.register(PromptTemplate)
admin.site.register(ImageGenerationJob)