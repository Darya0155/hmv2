from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("hotel/", views.hotel, name="hotel_info"),    





]