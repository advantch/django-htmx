from django.core.management.base import BaseCommand

from apps.mybnb.business_logic import index_homes


class Command(BaseCommand):
    help = "Index all homes in your database."

    def handle(self, *args, **options):
        index_homes()
