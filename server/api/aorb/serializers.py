from rest_framework import serializers
from .models import AorB


class AorbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AorB
        fields = '__all__'
