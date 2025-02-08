from django.forms import ValidationError
from rest_framework import serializers
from .models import RemisionCaso

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemisionCaso
        fields = '__all__'
        
        def create(self, validated_data):
            # Instanciar el modelo con los datos validados
            instance = RemisionCaso(**validated_data)
            # Ejecutar las validaciones definidas en clean()
            try:
                instance.full_clean()
            except ValidationError as e:
                raise serializers.ValidationError(e.message_dict)
            instance.save()
            return instance