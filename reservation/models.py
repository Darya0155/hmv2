from django.db import models
from hotel.models import Hotel
from room.models import Room
from guest.models import Guest


class ReservationStatus(models.TextChoices):
    CHECKIN = "check_in", "Check In"
    CANCELED = "canceled", "Canceled"
    CHECKOUT = "check_out", "Check Out"

# Create your models here.
class Reservation(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='reservations')
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey(Room,on_delete=models.CASCADE,related_name='reservations')
    status = models.CharField(max_length=30,choices=ReservationStatus.choices,default=ReservationStatus.CHECKIN)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.room.room_number} - {self.check_in}'



class ReservationGuest(models.Model):
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name='reservation_guests')
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE,related_name='reservation_guests')
    def __str__(self):
        return f'{self.guest.name} - {self.reservation.id}'


