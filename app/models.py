from django.conf import settings
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    id_flight = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type_flight = models.TextField()
    price = models.IntegerField()

    def register(self):
        self.save()

    def __str__(self):
        return self.name   