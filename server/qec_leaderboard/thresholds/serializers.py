from rest_framework import serializers
from .models import Threshold


class ThresholdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Threshold
        fields = ('id', 'code', 'decoder', 'noise_model', 'decoder_params',
                  'noise_model_params', 'threshold_value', 'threshold_std',
                  'paper_link', 'comment')
