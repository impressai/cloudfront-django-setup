from rest_framework.serializers import ModelSerializer
from .models import PublicImage, PrivateImage

class PublicImageModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    class Meta:
        model = PublicImage
        fields = '__all__'


class PrivateImageModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    class Meta:
        model = PrivateImage
        fields = '__all__'
