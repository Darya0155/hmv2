from datetime import datetime
from decimal import Decimal
from zoneinfo import ZoneInfo

from django.db.models import Model
from django.shortcuts import render, redirect
from django.db.models import Q

import reservation
from guest.forms import GuestForm
from guest.models import Guest
from transactions.models import Transaction
from .forms import ReservationForm,ReservationUpdateForm,FilterFormForReservation
from room.models import Room, RoomStatus
from hotel.views import getHotel
from .models import Reservation,ReservationGuest,ReservationStatus, ReservationStatusWithAll
from addons.models import Addon
from transactions.forms import AddOnTransactionForm


# Create your views here.

def index(request):
    hotel=getHotel(request)
    reservations = Reservation.active_reservations(hotel)
    filterForm = FilterFormForReservation()
    error ={ "msg" : ""}
    if request.method == 'POST':
        filterForm = FilterFormForReservation(request.POST)
        if filterForm.is_valid():
            room_number=filterForm.cleaned_data['room_number']
            status=filterForm.cleaned_data['status']
            if room_number and status:
                room = Room.find_room_by_number(hotel,room_number)
                if status==ReservationStatusWithAll.ALL:
                    reservations = Reservation.find_by_room(room)
                else:
                    reservations = Reservation.find_by_room_and_status(hotel,room,status)
            elif room_number:
                room = Room.find_room_by_number(hotel,room_number)
                reservations = Reservation.find_by_room(room)
            elif status:
                if status==ReservationStatusWithAll.ALL:
                    reservations = Reservation.find_all(hotel)
                else:
                    reservations = Reservation.find_by_status(hotel,status)
    return render(request, 'reservation/index.html',{'reservations':reservations,"ReservationStatus":ReservationStatus,"filterForm":filterForm,"error":error})

def new_booking(request):
    rooms = Room.objects.filter(status=RoomStatus.AVAILABLE).all()
    form = ReservationForm(initial={'room':rooms})

    hotel = getHotel(request)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.hotel = hotel
            reservation.save()
            selected=reservation.room
            selected.status = RoomStatus.OCCUPIED
            selected.save()
            Transaction.createRoomTransaction(reservation)
            return redirect(f"/reservation/booking/{reservation.id}")
    return render(request, 'reservation/newBooking.html',{'form':form,'available_rooms':rooms})

def edit_booking(request, bookingId):
    reservation = Reservation.objects.get(id=bookingId)
    hotel = getHotel(request)
    addons=Addon.find_all_available(hotel)
    mapResverationAndGuest(request, reservation)
    unmapResverationAndGuest(request, reservation)
    add_new_guest(request, reservation, hotel)
    updateReservation(request, reservation)
    add_on_transaction_creation(request, reservation, hotel)
    transactions:list[Transaction]=Transaction.find_all_by_reservation(reservation)
    total=calculate_total_from_allTransaction(transactions)
    balance = total-float(reservation.total_amount_recived)
    context = { 'reservation':reservation,
                'guest_search_list':search_guest(request,hotel),
                'current_guest_list':currentGuest(reservation),
                'add_new_guest_form':GuestForm(),
                'reservation_update_form':ReservationUpdateForm(instance=reservation),
                'transactions':transactions,
                'addons':addons,
                'total_price':total,
                'balance':balance,
                "addon_transaction_form":AddOnTransactionForm()}
    return render(request, 'reservation/editBooking.html',
                  context)

def calculate_total_from_allTransaction(transactions:list[Transaction]):
    total=float(0.0)
    for transaction in transactions:
        total+=float(transaction.total_price)
    return total

def add_on_transaction_creation(request,reservation,hotel):
    if request.method == 'POST':
        addon_id=request.POST.get('addon')
        quantity=request.POST.get('quantity')

        if addon_id:
            selected_add_on:Addon=Addon.objects.get(pk=addon_id)
            Transaction.createAddOnCranaction(reservation,selected_add_on,quantity,selected_add_on.__str__())



def add_new_guest(request,reservation,hotel):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.hotel=hotel
            guest.save()
            ReservationGuest.objects.update_or_create(reservation=reservation,guest=guest)


def updateReservation(request,reservation:Reservation):
    if request.method == 'POST':
       reservation.total_amount_recived+=float(request.POST.get('partialPaymentAmount',0))
       form= ReservationUpdateForm(request.POST,instance=reservation)
       if form.is_valid():
           form.save()


def search_guest(request,hotel):
    guest_search = request.GET.get('guest_search')
    if guest_search:
        return Guest.objects.filter(Q(id_value=guest_search) & Q(hotel=hotel)).all()
def currentGuest(reservation:Reservation):
    return [i for i in reservation.guests.all()]
def mapResverationAndGuest(request,reservation):
    add_searched_guest = request.GET.get('add_searched_guest')
    if add_searched_guest:
        guest=Guest.objects.get(pk=add_searched_guest)
        reservation.guests.add(guest)
def unmapResverationAndGuest(request,reservation):
    delete_current_guest = request.GET.get('delete_current_guest')
    if delete_current_guest:
        guest=Guest.objects.get(pk=delete_current_guest)
        reservation.guests.remove(guest)


def checkout_booking(request, bookingId):
    reservation = Reservation.objects.get(id=bookingId)
    if request.method == 'POST':
        reservation.status =ReservationStatus.CHECKOUT
        reservation.save()
        room=reservation.room
        room.status=RoomStatus.CLEANING
        room.save()
        return redirect('reservation_view')
    room = reservation.room
    hotel = reservation.hotel
    transactions = Transaction.find_all_by_reservation(reservation)
    total_amount=calculate_total_from_allTransaction(transactions)
    guests = currentGuest(reservation)
    context = { 'reservation':reservation,'room':room,'hotel':hotel,'transactions':transactions,"guests":guests,"total_amount":total_amount }
    return render(request, 'reservation/checkout.html',context)
