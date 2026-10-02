import math
from typing import Any

from django.db import models
from django.db.models import Q

from hotel.models import Hotel
from room.models import Room
from guest.models import Guest


class ReservationStatus(models.TextChoices):
    CHECKIN = "check_in", "Check In"
    CANCELED = "canceled", "Canceled"
    CHECKOUT = "check_out", "Check Out"


class ReservationStatusWithAll(models.TextChoices):
    ALL = "all", "All Reservations"
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
    total_amount_recived = models.FloatField(default=0)
    remarks = models.TextField(default="",blank=True, null=True)
    guests = models.ManyToManyField(through="ReservationGuest",to=Guest)
    def __str__(self):
        return f'{self.room.room_number} - {self.check_in}'
    @property
    def days(self):
        duration = self.check_out - self.check_in
        return math.ceil(duration.total_seconds() / (24 * 60 * 60))
    @staticmethod
    def active_reservations(hotel:Hotel)->list:
        return [i for i in Reservation.objects.filter(Q(hotel=hotel) & Q(status=ReservationStatus.CHECKIN)).all()]
    @staticmethod
    def get_reservations(hotel:Hotel)->list:
        return [i for i in Reservation.objects.filter(Q(hotel=hotel)).all()]
    def find_by_room(room:Room)->list:
        return [i for i in Reservation.objects.filter(Q(room=room)).all()]
    @staticmethod
    def find_by_room_and_status(hotel:Hotel,room:Room, status:ReservationStatus)->list:
        return [i for i in Reservation.objects.filter(Q(hotel=hotel) & Q(room=room) & Q(status=status)).all()]
    @staticmethod
    def find_all(hotel:Hotel)->list:
        return [i for i in Reservation.objects.filter(Q(hotel=hotel)).all()]
    @staticmethod
    def find_by_status(hotel:Hotel, status:ReservationStatus)->list:
        return [i for i in Reservation.objects.filter(Q(hotel=hotel) & Q(status=status)).all()]

class ReservationGuest(models.Model):
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.guest.name} - {self.reservation.id}'



