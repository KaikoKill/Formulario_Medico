from rest_framework import serializers
from .models import RemisionCaso

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemisionCaso
        fields = '__all__'