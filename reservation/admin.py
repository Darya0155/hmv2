from django.contrib import admin
from .models import ReservationGuest,Reservation
# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('room','check_in','check_out')

@admin.register(ReservationGuest)
class ReservationGuestAdmin(admin.ModelAdmin):
    list_display = ('reservation','guest')