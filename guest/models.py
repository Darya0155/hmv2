from django.db import models
from hotel.models import Hotel


class IdType(models.TextChoices):
    ADHAR = "adhar_card", "Adhar Card"
    DRIVING = "driving_card", "Driving Card"
    VOTER_CARD = "voter_card", "Voter Card"
    OTHER = "other", "Other"

class GendarChoise(models.TextChoices):
    Male = "male", "Male"
    Female = "female", "Female"
    other = "other", "Other"

class Guest(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='guests')
    name = models.CharField(max_length=100)
    gender = models.TextField(choices=GendarChoise.choices,default=GendarChoise.Male,blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=10,default="1234567890")
    email = models.EmailField(default='nomail@localhost.com')
    id_type = models.CharField(max_length=20,choices=IdType.choices,default=IdType.ADHAR)
    id_value = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name} - {self.id}'