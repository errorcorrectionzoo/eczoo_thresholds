from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class NoiseModel(models.Model):
    name = models.CharField(max_length=255)
    params = models.JSONField()
    paper_link = models.CharField(max_length=255)
    description = models.CharField(max_length=2047, blank=True)