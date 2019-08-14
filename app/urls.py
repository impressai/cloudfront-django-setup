from rest_framework.routers import DefaultRouter
from .views import PublicImageModelViewSet, PrivateImageModelViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'public_image', PublicImageModelViewSet, base_name='public_image')
router.register(r'private_image', PrivateImageModelViewSet, base_name='private_image')


urlpatterns = router.urls