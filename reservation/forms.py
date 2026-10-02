import datetime
from datetime import timedelta
from time import timezone
from zoneinfo import ZoneInfo

from django.forms import ModelForm, DateInput,Form
from django import forms
from django.forms.widgets import TextInput, DateTimeInput
from django.utils import timezone

from reservation.models import Reservation,ReservationStatusWithAll, ReservationStatus
from room.models import Room


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['hotel','guests']
        widgets = {
            'check_in': DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'check_out': DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        india_tz = ZoneInfo("Asia/Kolkata")
        now = datetime.datetime.now(india_tz)

        self.initial['check_in'] = now.strftime('%Y-%m-%dT%H:%M')

        checkout = now + timedelta(days=1)
        checkout = checkout.replace(
            hour=11,
            minute=0,
            second=0,
            microsecond=0
        )

        self.initial['check_out'] = checkout.strftime('%Y-%m-%dT%H:%M')
        self.fields['room'].queryset = Room.get_available_rooms()


class ReservationUpdateForm(ModelForm):
    partialPaymentAmount = forms.FloatField(required=False,label="Payment Amount",
                                            widget=forms.NumberInput(attrs={'class':'form-control',"value":0}))
    class Meta:
        model = Reservation
        fields = '__all__'
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['hotel','status','room','check_in','total_amount_recived','guests']
        widgets = {
            'check_out': DateInput(attrs={'type': 'date','class':'datepicker'}),
        }
        readonly_fields = ['check_in','check_out','room']

class FilterFormForReservation(Form):
    room_number=forms.CharField(label='Room Number',widget=TextInput(attrs={'class':'form-control'}),required=False)
    status=forms.fields.ChoiceField(label='Status',required=False,choices=ReservationStatusWithAll)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['status']=ReservationStatus.CHECKIN
