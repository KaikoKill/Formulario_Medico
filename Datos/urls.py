from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/Datos', ProjectViewSet, 'Datos')

urlpatterns = router.urls