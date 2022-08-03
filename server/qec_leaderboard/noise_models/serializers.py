from rest_framework import serializers
from .models import NoiseModel


class NoiseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = NoiseModel
        fields = ('id', 'name', 'params', 'paper_link', 'description', 'zoo_link')