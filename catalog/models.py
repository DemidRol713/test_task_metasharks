from django.db import models


class BrandAuto(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ModelAuto(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(BrandAuto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.name}'


class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name