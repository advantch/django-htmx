import random

from factory.django import DjangoModelFactory
from faker import Faker as Fake

from apps.search_metrics.models import SearchMetric


class SearchMetricFactory(DjangoModelFactory):
    class Meta:
        model = SearchMetric

    client_ip = Fake().ipv4_public()
    search_term = Fake().paragraph(nb_sentences=1)[:30]
    hits = random.randint(100, 10000)
