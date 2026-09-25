from django.contrib import admin
from .models import Guest

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','address',"id_type","id_value")
    search_fields = ('name','address','id_value')
