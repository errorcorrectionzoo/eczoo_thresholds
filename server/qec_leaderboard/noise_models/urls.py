from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('noise_models/', views.NoiseModelList.as_view()),
    path('noise_models/<int:pk>/', views.NoiseModelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)