from django.core.management.base import BaseCommand

from apps.mybnb.business_logic import clear_index


class Command(BaseCommand):
    help = "Index all homes in your database."

    def handle(self, *args, **options):
        clear_index()
