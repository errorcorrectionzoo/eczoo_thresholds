from rest_framework import serializers
from .models import Decoder


class DecoderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Decoder
        fields = ('id', 'name', 'params', 'paper_link', 'description')