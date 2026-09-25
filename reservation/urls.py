from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="reservation_view"),
    path("newBooking", views.new_booking, name="new_booking"),
    path("booking/<bookingId>", views.edit_booking, name="add_guest"),
    # path("<room_id>/delete", views.delete_room, name="guest_delete_view"),
]