import datetime

from django.forms import ModelForm, DateInput

from reservation.models import Reservation
from room.models import Room


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['hotel']
        widgets = {
            'check_in': DateInput(attrs={'type': 'date','class':'datepicker',"value":datetime.date.today()}),
            'check_out': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.get_available_rooms()

