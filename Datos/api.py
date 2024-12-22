from .models import RemisionCaso
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = RemisionCaso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save()
