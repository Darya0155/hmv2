from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='addon_view'),
    path('add', views.add_new_addon, name='add_addon_view'),
    path('<id>/edit', views.edit_new_addon, name='edit_addon_view'),


]