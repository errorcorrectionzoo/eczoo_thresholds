from rest_framework import serializers
from .models import Code


class CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Code
        fields = ('id', 'name', 'is_parent', 'adjacent_codes', 'paper_link', 'zoo_link')