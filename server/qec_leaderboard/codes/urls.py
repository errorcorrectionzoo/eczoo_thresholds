from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('codes/', views.CodeList.as_view()),
    path('codes/<int:pk>/', views.CodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)