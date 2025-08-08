# from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
# rest_framework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.views import APIView

from django.core.serializers.json import DjangoJSONEncoder

# app imports
from .models import ImageGenerationJob
from .serializer import ImageGenerationSerializer

# auxiliary imports
import os
import json
import requests
from dotenv import load_dotenv
import time
from datetime import datetime

# helper functions
from utils.hd_image import _hd_image_gen


# load environment variable
load_dotenv()

# Generate image CBV(class-based view)

class GenerateImage(ModelViewSet):
    queryset = ImageGenerationJob.objects.all()
    serializer_class = ImageGenerationSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # get required data from serializer
            prompt = serializer.validated_data.get('prompt')
            # api_key = os.getenv('')
            api_key = '4cc076ec958d4dbc9312dc3b5982cb92'
            # Pass it to the helper generation function
            generation = _hd_image_gen(api_key=api_key, prompt=prompt)
            # get the returned data from generation
            completed_at = datetime.now()
            image_url = generation.get('result', [{}])[0].get('urls', [None])[0]
            enhanced_prompt = generation.get('result', [{}])[0].get('enhanced_prompt', [None])
            # seed_used = ''
            # uuid = ''



            serializer.save(prompt=prompt, image_url=image_url, enhanced_prompt=enhanced_prompt, completed_at=completed_at)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

    

        
@csrf_exempt
def test(request):
    if request.method == 'POST':
        bria_api_key = "4cc076ec958d4dbc9312dc3b5982cb92"
        prompt = request.POST.get('prompt')

        if not bria_api_key:
            return Response({"error": "Provide Brai API key"})

        generation = _hd_image_gen(api_key=bria_api_key, prompt=prompt)

        if isinstance(generation, Exception):
            return JsonResponse({"error": str(generation)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse(generation)
    return JsonResponse({"error": "NOT accepting GET request Now."}, status.HTTP_400_BAD_REQUEST)