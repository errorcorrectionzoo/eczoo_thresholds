from django.db import models
from ..codes.models import Code
from ..decoders.models import Decoder
from ..noise_models.models import NoiseModel

class Threshold(models.Model):
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    decoder = models.ForeignKey(Decoder, on_delete=models.CASCADE)
    decoder_params = models.JSONField()
    noise_model = models.ForeignKey(NoiseModel, on_delete=models.CASCADE)
    noise_model_params = models.JSONField()
    threshold_value = models.FloatField()
    threshold_std = models.FloatField()
    paper_link = models.CharField(max_length=255)
    comment = models.CharField(max_length=2047)