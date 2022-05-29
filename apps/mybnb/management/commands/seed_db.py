import os
import json
import logging
import random
import time

import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker

from apps.mybnb.models import Home

logger = logging.getLogger(__name__)


def fetch_images_from_unsplash(limit=1000, query="houses"):
    """Fetches images from unsplash"""
    data = {"total": 10000, "fetched": 24}
    results = []
    API_URL = "https://api.unsplash.com/search/photos/"

    for page in range(1, 25):
        url = (
            f"{API_URL}?query={query}&per_page=30&page={page}&"
            f"client_id={settings.UNSPLASH_API_KEY}"
        )
        response = requests.get(url)
        time.sleep(2)
        results.extend(response.json()["results"])

    data.update({"results": results})
    file_path = os.path.join(settings.BASE_DIR,"json_data.json")
    with open(file_path) as o:
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
    file_path = os.path.join(settings.BASE_DIR,"json_data.json")
    f = open(file_path)
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
