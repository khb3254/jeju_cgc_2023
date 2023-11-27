from django.db import models

class Jeju(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title

class CropMarketData(models.Model):
    crop_type = models.CharField(max_length=20)
    supplier = models.CharField(max_length=20, blank=True)
    origin = models.CharField(max_length=20, blank=True)
    crop_date = models.DateField(null=False)
    crop_supply = models.IntegerField(null=True)
    crop_price = models.IntegerField(null=True)

class PredictionData(models.Model):
    crop_type = models.CharField(max_length=20)
    supplier = models.CharField(max_length=20, blank=True)
    origin = models.CharField(max_length=20, blank=True)
    crop_date = models.DateField(null=False)
    crop_price = models.IntegerField(null=False)
    ai_model = models.CharField(max_length=30, null=False, blank=False)