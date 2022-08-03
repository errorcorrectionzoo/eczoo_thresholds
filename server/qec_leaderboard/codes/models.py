from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Code(models.Model):
    name = models.CharField(max_length=255)
    is_parent = models.BooleanField()
    adjacent_codes = models.JSONField()
    paper_link = models.CharField(max_length=255)
    zoo_link = models.CharField(max_length=255, blank=True)