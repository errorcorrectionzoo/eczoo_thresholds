from rest_framework import generics
from .models import Decoder
from .serializers import DecoderSerializer

class DecoderList(generics.ListCreateAPIView):
    queryset = Decoder.objects.all()
    serializer_class = DecoderSerializer


class DecoderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decoder.objects.all()
    serializer_class = DecoderSerializer