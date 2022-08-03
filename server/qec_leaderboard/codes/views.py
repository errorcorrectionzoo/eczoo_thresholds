from rest_framework import generics
from .models import Code
from .serializers import CodeSerializer

class CodeList(generics.ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer


class CodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer