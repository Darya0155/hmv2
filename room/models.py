from django.db import models
from hotel.models import Hotel

# Create your models here.
class RoomType(models.TextChoices):
    SINGLE = "single", "Single Room"
    DOUBLE = "double", "Double Room"
    DELUXE = "deluxe", "Deluxe Room"
    SUITE = "suite", "Suite"
    FAMILY = "family", "Family Room"

class RoomStatus(models.TextChoices):
    AVAILABLE = "available", "Available"
    OCCUPIED = "occupied", "Occupied"
    RESERVED = "reserved", "Reserved"
    MAINTENANCE = "maintenance", "Maintenance"
    CLEANING = "cleaning", "Cleaning"
    OUT_OF_SERVICE = "out_of_service", "Out of Service"



class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='rooms')
    room_number = models.IntegerField()
    per_night_price=models.FloatField()
    state_tax_percentage=models.FloatField()
    center_tax_percentage=models.FloatField()
    room_type=models.CharField(max_length=30,choices=RoomType.choices,default=RoomType.SINGLE)
    status=models.CharField(max_length=30,choices=RoomStatus.choices,default=RoomStatus.AVAILABLE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    @property
    def subtotal(self):
        return self.per_night_price

    @property
    def state_tax_amount(self):
        return self.subtotal * self.state_tax_percentage / 100

    @property
    def central_tax_amount(self):
        return self.subtotal * self.center_tax_percentage / 100

    @property
    def total_price(self):
        return (
            self.subtotal
            + self.state_tax_amount
            + self.central_tax_amount
        )
    def __str__(self):
        return str(self.room_number)

    @staticmethod
    def get_available_rooms():
        return Room.objects.filter(status=RoomStatus.AVAILABLE)