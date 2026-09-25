from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RoomForm
from .models import Room
from django.contrib.auth import logout
from hotel.views import getHotel

# Create your views here.
@login_required
def room(request):
    form = RoomForm()
    hotel =getHotel(request)
    rooms = []
    if hotel is not None:
        rooms = hotel.rooms.all()
    else:
        logout(request)
    return render(request, "room/index.html", {"rooms":rooms,"form": form,"error":" Please enter a valid room."})

@login_required
def add_room(request):
    form = RoomForm()
    hotel =getHotel(request)
    if request.method == "POST" :
        form = RoomForm(request.POST)
        if form.is_valid():
            saved_room = form.save(commit=False)
            saved_room.hotel=hotel
            saved_room.save()
            return redirect(to="/room/")
        else:
            form = RoomForm(instance=form)
    return render(request, "room/add.html", {"form": form,"error":" Please enter a valid room."})


@login_required
def edit_room(request,room_id):
    room = Room.objects.get(pk=room_id)
    form = RoomForm(instance=room)
    hotel =getHotel(request)
    if request.method == "POST" :
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            saved_room = form.save(commit=False)
            saved_room.hotel=hotel
            saved_room.save()
            return redirect(to="/room/")
        else:
            form = RoomForm(instance=room)
    return render(request, "room/edit.html", {"form": form})

@login_required
def delete_room(request,room_id):
    room = Room.objects.get(pk=room_id)
    room.delete()
    return redirect(to="/room/")
