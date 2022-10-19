from django.db import models
from django.utils import timezone

from catalog.models import BrandAuto, ModelAuto, Color


class Order(models.Model):

    brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE, blank=False)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE, blank=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False)
    date_created = models.DateField(default=timezone.now)