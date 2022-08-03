from rest_framework import generics
from .models import Threshold
from .serializers import ThresholdSerializer

class ThresholdList(generics.ListCreateAPIView):
    queryset = Threshold.objects.all()
    serializer_class = ThresholdSerializer


class ThresholdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Threshold.objects.all()
    serializer_class = ThresholdSerializer