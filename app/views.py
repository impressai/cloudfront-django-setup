from rest_framework.viewsets import ModelViewSet

from django.views.generic.base import TemplateView

from .serializers import PublicImageModelSerializer, PrivateImageModelSerializer
from .models import PublicImage, PrivateImage
# Create your views here.

class PublicImageModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing PublicImage.
    """
    queryset = PublicImage.objects.all()
    serializer_class = PublicImageModelSerializer


class PrivateImageModelViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing PrivateImage.
    """
    queryset = PrivateImage.objects.all()
    serializer_class = PrivateImageModelSerializer



class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        context['message'] = 'Hello World!'
        context['public_images'] = PublicImage.objects.all()
        context['private_images'] = PrivateImage.objects.all()
        return context
