from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import HttpDog

class HttpDogModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    class Meta:
        model = HttpDog
        fields = '__all__'
