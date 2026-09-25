from django.contrib.auth.decorators import login_required
from django.db.models.query_utils import Q
from django.shortcuts import render,redirect
from .forms import GuestForm
from hotel.views import getHotel
from .models import Guest
from hotel.models import Hotel
# Create your views here.
# Guest

@login_required
def add_guest(request):
    form = GuestForm()
    hotel = getHotel(request)
    if request.method == "POST" :
        form = GuestForm(request.POST)
        if form.is_valid():
            saved_room = form.save(commit=False)
            saved_room.hotel=hotel
            saved_room.save()
            return redirect(to="/guest/")
        else:
            form = GuestForm(instance=form)
    return render(request, "hotel/guest/add.html", {"form": form,"error":" Please enter a valid room."})
@login_required
def guest_edit(request, guest_id):
    guest = Guest.objects.get(pk=guest_id)
    form = GuestForm(instance=guest)
    hotel =getHotel(request)
    if request.method == "POST" :
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            saved_guest = form.save(commit=False)
            saved_guest.hotel=hotel
            saved_guest.save()
            return redirect(to="/guest/")
        else:
            form = GuestForm(instance=guest)
    return render(request,'hotel/guest/edit.html', {"guest":guest,"form":form})

@login_required
def guest(request):
    hotel =getHotel(request)
    guests = Guest.objects.filter(hotel=hotel).all()
    searchId=""
    if request.method == "POST" :
        searchId=request.POST.get("idvalue")
        guests=Guest.objects.filter(Q(id_value=request.POST.get("idvalue")) & Q(hotel=hotel)).all()
    return render(request, "hotel/guest/index.html", {"guests":guests,"idvalue":searchId})