from rest_framework import serializers

# core app imports
from .models import PromptTemplate, ImageGenerationJob


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
    image_gen_type = serializers.ChoiceField(
        choices=GENERATION_TYPE_CHOICES
    )
    model_version = serializers.ChoiceField(
        choices=[]
    )
    class Meta:
        model = ImageGenerationJob
        fields = "__all__"

    
    def validate(self, data):
        gen_type = data.get('image_gen_type')
        version = data.get('model_version')
        allowed = ALLOWED_MODEL_VERSIONS.get(gen_type, [])

        if version not in allowed:
            raise serializers.ValidationError({
                'model_version': (
                    f"‘{version}’ isn’t valid for “{gen_type}” – allowed: {', '.join(allowed)}"
                )
            })
        return data

class PromptTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromptTemplate
        fields = "__all__"