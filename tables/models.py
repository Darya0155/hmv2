from django.db import models
from django.db.models.query_utils import Q

from hotel.models import Hotel

class TableStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE'
    OCCUPIED = 'OCCUPIED'
    RESERVED = 'RESERVED'

# Create your models here.
class Table(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='tables')
    table_number = models.IntegerField()
    description = models.TextField()
    status=models.CharField(max_length=30,choices=TableStatus.choices,default=TableStatus.AVAILABLE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.table_number)

    @staticmethod
    def get_available_tables():
        return Table.objects.filter(status=TableStatus.AVAILABLE)
    @staticmethod
    def find_table_by_number(hotel,number):
        return Table.objects.get(Q(hotel=hotel) & Q(table_number=number))