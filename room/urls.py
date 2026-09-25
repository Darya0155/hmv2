from django.urls import path
from . import views

urlpatterns = [
    path('', views.room, name='room_view'),
    path('add', views.add_room, name='add_room_view'),
    path('<room_id>/edit', views.edit_room, name='edit_room_view'),
    path('<room_id>/delete', views.delete_room, name='delete_room_view'),

]