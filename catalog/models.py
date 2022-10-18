from django.db import models


class BrandAuto(models.Model):
    name = models.CharField(max_length=30)


class ModelAuto(models.Model):
    name = models.CharField(max_length=50)
    brand_id = models.ForeignKey(BrandAuto, on_delete=models.CASCADE)


class Color(models.Model):
    name = models.CharField(max_length=30)