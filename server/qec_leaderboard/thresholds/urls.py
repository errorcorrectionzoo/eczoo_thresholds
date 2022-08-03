from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('thresholds/', views.ThresholdList.as_view()),
    path('thresholds/<int:pk>/', views.ThresholdDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)