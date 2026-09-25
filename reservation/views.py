from django.db.models import Model
from django.shortcuts import render, redirect
from .forms import ReservationForm
from room.models import Room, RoomStatus
from hotel.views import getHotel
from .models import Reservation


# Create your views here.

def index(request):
    reservations = Reservation.objects.all().order_by('create_at')
    return render(request, 'reservation/index.html',{'reservations':reservations})

def new_booking(request):
    rooms = Room.objects.filter(status=RoomStatus.AVAILABLE).all()
    form = ReservationForm(initial={'room':rooms})

    hotel = getHotel(request)
    print(hotel)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.hotel = hotel
            reservation.save()
            selected=reservation.room
            selected.status = RoomStatus.OCCUPIED
            selected.save()
            return redirect(f"/reservation/booking/{reservation.id}/addGuest")
    return render(request, 'reservation/newBooking.html',{'form':form,'available_rooms':rooms})

def edit_booking(request, bookingId):
    reservation = Reservation.objects.get(id=bookingId)
    return render(request, 'reservation/editBooking.html',{'reservation':reservation})


