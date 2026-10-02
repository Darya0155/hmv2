from django.db import models
from django.db.models import Q
from rest_framework import status

from hotel.models import Hotel



# Create your models here.
class AddOnStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'

class Addon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='addons')
    price=models.FloatField()
    state_tax_percentage=models.FloatField()
    center_tax_percentage=models.FloatField()
    status=models.CharField(max_length=30,choices=AddOnStatus.choices,default=AddOnStatus.AVAILABLE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    def __str__(sef):
        return f"{sef.name}-{sef.price}"
    @staticmethod
    def find_all(hotel):
        return Addon.objects.filter(hotel=hotel).all()
    @staticmethod
    def find_all_available(hotel):
        return Addon.objects.filter(Q(hotel=hotel) & Q(status=AddOnStatus.AVAILABLE)).all()