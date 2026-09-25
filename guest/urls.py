from django.urls import path
from . import views

urlpatterns = [

    path("", views.guest, name="guest_view"),
    path("add", views.add_guest, name="add_guest_view"),
    path("<guest_id>/edit", views.guest_edit, name="guest_edit_view"),
    # path("<room_id>/delete", views.delete_room, name="guest_delete_view"),

]