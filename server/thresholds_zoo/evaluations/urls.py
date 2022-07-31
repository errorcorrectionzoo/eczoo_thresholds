from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('evaluations/', views.EvaluationList.as_view()),
    path('evaluations/<int:pk>/', views.EvaluationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)