from rest_framework import generics
from .models import NoiseModel
from .serializers import NoiseModelSerializer

class NoiseModelList(generics.ListCreateAPIView):
    queryset = NoiseModel.objects.all()
    serializer_class = NoiseModelSerializer


class NoiseModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoiseModel.objects.all()
    serializer_class = NoiseModelSerializer