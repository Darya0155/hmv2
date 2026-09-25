from django import forms
from .models import Guest

# Register your models here.
class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'
        exclude = ['created_at','update_at','hotel']