

from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import HotelUser
from .forms import HotelForm
from django.db.models import Q


# Create your views here.
@login_required
def index(request):
    return render(request,"hotel/index.html")


@login_required
def hotel(request):
    hotel=getHotel(request)
    print(hotel)
    form=None
    if request.method == "POST":
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            saved_hotel = form.save()
            HotelUser.objects.update_or_create(hotel=saved_hotel,user=request.user)
            hotel = saved_hotel    
    else:
        form = HotelForm(instance=hotel)
    return render(request, "hotel/hotel.html", {"form": form, "hotel": hotel})

def getHotel(request):
    try:
        r =request.user.hotel_users.all()
        print(r)
        return r[0].hotel
    except Exception as e:
        print(e)
        return None


