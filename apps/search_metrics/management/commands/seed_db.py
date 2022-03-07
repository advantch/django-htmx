import random

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from faker import Faker

from apps.search_metrics.factories import SearchMetricFactory
from apps.search_metrics.models import SearchMetric

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with sample data."

    @transaction.atomic
    def handle(self, *args, **options):
        if SearchMetric.objects.exists():
            raise CommandError(
                "This command cannot be run when any "
                "Search Metrics exist, to guard "
                + "against accidental use on production."
            )
        self.stdout.write("Seeding database...")
        mock_search_metrics()
        self.stdout.write("Done.")


def mock_search_metrics(rows=1000):
    for i in range(rows):
        Faker.seed(random.randint(100, 10000))
        obj = SearchMetric(
            client_ip=fake.ipv4_public(),
            search_term=fake.paragraph(nb_sentences=1)[:30],
            hits=random.randint(100, 10000),
        )
        obj.save()
    SearchMetricFactory.create_batch(rows)
