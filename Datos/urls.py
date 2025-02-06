from django.conf import settings
from rest_framework import routers
from .api import ProjectViewSet
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('api/Datos', ProjectViewSet, 'Datos')

urlpatterns = router.urls
