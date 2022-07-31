from django.db import models

class Evaluation(models.Model):
    code_name = models.CharField(max_length=255)
    decoder_name = models.CharField(max_length=255)
    noise_model_name = models.CharField(max_length=255)
    threshold_value = models.FloatField()