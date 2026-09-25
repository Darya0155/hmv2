from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    gst_number = models.CharField(max_length=100, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.id}'


class HotelUser(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        related_name='hotel_users'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='hotel_users'
    )


    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"





