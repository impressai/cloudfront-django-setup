from rest_framework.routers import DefaultRouter
from .views import HttpDogModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'http_dog', HttpDogModelViewSet, base_name='http_dog')


urlpatterns = router.urls