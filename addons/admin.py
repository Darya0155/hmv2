from django.contrib import admin

from addons.models import Addon
from hotel.models import Hotel


# Register your models here.
@admin.register(Addon)
class AddonAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)