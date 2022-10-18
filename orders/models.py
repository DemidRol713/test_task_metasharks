from django.db import models
from django.utils import timezone

from catalog.models import BrandAuto, ModelAuto, Color
from user.models import Profile


class Order(models.Model):

    brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)