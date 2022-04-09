from django.db import models
from model_utils.models import UUIDModel


class HomeManager(models.Manager):
    def get_index_objects(self):
        """Objects formatted for indexing"""
        return [h.dict() for h in self.get_queryset()]

    def get_filter_attributes(self):
        """A dict of filterable attributes"""
        qs = self.get_queryset()
        return {
            "countries": list(set(qs.values_list("country", flat=True))),
            "cities": list(set(qs.values_list("city", flat=True))),
        }


class Home(UUIDModel):
    address = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=100)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500, default="")

    objects = HomeManager()

    def dict(self):
        return {
            "id": str(self.id),
            "address": self.address,
            "price": float(self.price),
            "city": self.city,
            "country": self.country,
            "image_url": self.image_url,
        }
