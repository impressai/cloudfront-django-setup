from rest_framework.viewsets import ModelViewSet
from .serializers import HttpDogModelSerializer
from .models import HttpDog
# Create your views here.

class HttpDogModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing HttpDog.
    """
    queryset = HttpDog.objects.all()
    serializer_class = HttpDogModelSerializer