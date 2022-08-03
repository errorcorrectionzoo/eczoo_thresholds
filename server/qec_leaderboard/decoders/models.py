from django.db import models

class Decoder(models.Model):
    name = models.CharField(max_length=255)
    params = models.JSONField()
    paper_link = models.CharField(max_length=255)
    description = models.CharField(max_length=2047, blank=True)