from django import forms
from .models import Hotel,HotelUser


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'address', 'phone_number', 'email', 'gst_number']


