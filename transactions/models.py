from django.db import models

import transactions
from addons.models import Addon
from reservation.models import Reservation
from room.models import Room


# Create your models here.

class TransactionType(models.TextChoices):
    ROOM = 'ROOM'
    ADD_ON='ADD_ON'
    FOOD = 'FOOD'


class Transaction(models.Model):
    type=models.CharField(choices=TransactionType.choices,max_length=10,default=TransactionType.ROOM)
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name='transactions')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    state_tax_percentage=models.DecimalField(max_digits=10,decimal_places=2)
    central_tax_percentage=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    details=models.TextField(blank=True,null=True)
    @property
    def subtotal(self):
        return self.price * self.quantity

    @property
    def state_tax_amount(self):
        return self.subtotal * self.state_tax_percentage / 100
    @property
    def central_tax_amount(self):
        return self.subtotal * self.central_tax_percentage / 100

    @property
    def total_price(self):
        return (
                self.subtotal
                + self.state_tax_amount
                + self.central_tax_amount
        )

    def __str__(self):
        return f'{self.reservation} - {self.type}'

    @staticmethod
    def createRoomTransaction(reservation):
        room = reservation.room
        roomTransaction = Transaction.objects.create(reservation=reservation,type=TransactionType.ROOM,price=room.per_night_price,
                                   state_tax_percentage=room.state_tax_percentage,
                                          central_tax_percentage=room.center_tax_percentage,quantity=reservation.days,
                                          details=room.__str__())
        roomTransaction.save()
        return roomTransaction

    @staticmethod
    def updateRoomTransactionDays(reservation:Reservation,days):
        roomTransaction = Transaction.objects.get(reservation=reservation,type=TransactionType.ROOM)
        roomTransaction.quantity = days
        roomTransaction.save()
        return roomTransaction

    @staticmethod
    def createAddOnCranaction(reservation:Reservation, selected_add_on:Addon,quantity:int,details:str) -> Addon:
        add_on_price = Transaction.objects.create(reservation=reservation,type=TransactionType.ADD_ON,price=selected_add_on.price,
                                                     state_tax_percentage=selected_add_on.state_tax_percentage,
                                                     central_tax_percentage=selected_add_on.center_tax_percentage,quantity=quantity,
                                                     details=details)
        add_on_price.save()
        return add_on_price
    @staticmethod
    def find_all_by_reservation(reservation:Reservation)->list:
        return [i for i in Transaction.objects.filter(reservation=reservation).all()]


