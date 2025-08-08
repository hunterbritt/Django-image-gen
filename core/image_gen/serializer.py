from rest_framework import serializers

# core app imports
from .models import PromptTemplate, ImageGenerationJob


import random

GENERATION_TYPE_CHOICES = [
    ('base',   'Base'),
    ('fast',  'Fast-Gen'),
    ('vector', 'Vector'),
    ('hd',     'HD'),
]

ALLOWED_MODEL_VERSIONS = {
    'base':   ['2.2', '3.1', '3.2'],
    'fast':  ['1.0', '1.1'],
    'vector': ['v1',  'v2'],
    'hd':     ['3.2-hd', '4.0-hd'],
}

class ImageGenerationSerializer(serializers.ModelSerializer):
    # image_gen_type = serializers.ChoiceField(
    #     choices=GENERATION_TYPE_CHOICES,
    #     required=False,
    #     read_only=False,
    #     write_only=True
    # )
    # model_version = serializers.ChoiceField(
    #     choices=[],
    #     allow_null=True,
    #     required=False,
    #     read_only=True
    # )
    class Meta:
        model = ImageGenerationJob
        # fields = ['user', 'prompt', 'enhanced_prompt', 'status', 'image_url', 'bria_response']
        fields = "__all__"
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args,**kwargs)
    #     t = self.initial_data.get('image_gen_type') if hasattr(self, 'initial_data') else None
    #     if t in ALLOWED_MODEL_VERSIONS:
    #         self.fields['model_version'].choices = [(v,v) for v in ALLOWED_MODEL_VERSIONS[t]]
    
    # def validate(self, data):
    #     t = data.get('image_gen_type')
    #     v = data.get('model_version')

    #     allowed = ALLOWED_MODEL_VERSIONS.get(t, [])
    #     if not v:
    #         data['model_version'] = random.choice(allowed)
    #         print(data['model_version'])
    #     elif v not in allowed:
    #         raise serializers.ValidationError(
    #             {
    #                 "model_version": f"{v} is not a valid for {t}. Allowed: {''.join(allowed)}"
    #             }
    #         )
    #     return data

class PromptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptTemplate
        fields = "__all__"