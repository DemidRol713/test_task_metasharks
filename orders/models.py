from django.db import models
from django.utils import timezone

from catalog.models import BrandAuto, ModelAuto, Color


class Order(models.Model):

    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE, blank=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False)
    date_created = models.DateField(default=timezone.now)

    def get_amount_of_orders_with_color(self, color_id):
        """
        Возвращает количество заказов с определенным цветом
        """
        return Order.objects.filter(color=color_id).count()

    def get_amount_of_orders_with_brand_auto(self, brand_id):
        """
        Возвращает количество заказов с определенной маркой машин
        """
        return Order.objects.filter(model__brand=brand_id).count()
