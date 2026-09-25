from django.contrib import admin
from .models import Hotel,HotelUser

# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','address')

@admin.register(HotelUser)
class HotelUserAdmin(admin.ModelAdmin):
    list_display = ('user','hotel')



