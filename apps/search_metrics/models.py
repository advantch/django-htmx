from django.db import models
from model_utils.models import UUIDModel


# Create your models here.
class SearchMetric(UUIDModel):
    client_ip = models.GenericIPAddressField()
    hits = models.IntegerField(null=True)
    search_date = models.DateTimeField(auto_now_add=True)
    search_term = models.CharField(max_length=300, blank=True)
