from django.contrib import admin

from reservation.models import Reservation
from transactions.models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'type')
    search_fields = ('reservation', 'type')