from rest_framework import serializers
from api.models import Aorb


class AorbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aorb
        exclude = ['user']
