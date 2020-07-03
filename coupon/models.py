from django.db import models
from django.utils import timezone


class Shop(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Coupon(models.Model):
    number = models.IntegerField(unique=True)
    deadline = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=35))
    used = models.DateTimeField(blank=True, null=True)
    shop = models.ForeignKey(Shop, blank=True, null=True, on_delete=models.CASCADE)
