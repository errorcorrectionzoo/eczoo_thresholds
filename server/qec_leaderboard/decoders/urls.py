from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('decoders/', views.DecoderList.as_view()),
    path('decoders/<int:pk>/', views.DecoderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)