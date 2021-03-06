from django.db import models

class Address (models.Model):
    street = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.street