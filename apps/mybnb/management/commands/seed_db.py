import json
import random
import time
import logging

import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from faker import Faker

from apps.mybnb.models import Home

logger = logging.getLogger(__name__)


def fetch_images_from_unsplash(limit=1000, query="houses"):
    """Fetches images from unsplash"""
    data = {"total": 10000, "fetched": 24}
    results = []
    API_URL = "https://api.unsplash.com/search/photos/"

    for page in range(1, 25):
        url = f"{API_URL}?query={query}&per_page=30&page={page}&client_id={settings.UNSPLASH_API_KEY}"
        response = requests.get(url)
        time.sleep(2)
        results.extend(response.json()["results"])

    data.update({"results": results})
    with open(f"json_data.json", "w") as o:
        json.dump(data, o)
    return data


def fake_house_data():
    return {
        "address": Faker().address(),
        "city": Faker().city(),
        "country": Faker().country(),
        "price": round(random.uniform(500, 50000), 2),
    }


def generate_data():
    """Generate data"""
    logger.info("creating fake data...")
    f = open("json_data.json")
    data = json.load(f)
    f.close()
    for i in data["results"]:
        image_url = i["urls"]["small"]
        fake_data = fake_house_data()
        doc = Home(image_url=image_url, **fake_data)
        doc.save()


class Command(BaseCommand):
    help = "Seed database with sample data."
    
    def handle(self, *args, **options):
        generate_data()
