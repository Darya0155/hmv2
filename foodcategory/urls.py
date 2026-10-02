from django.urls import path
from . import views

urlpatterns = [
    path('category', views.foodCategory_index, name='foodCategory_index'),
    path('category/<category_id>/edit', views.foodCategory_edit, name='foodCategory_edit'),
    path('category/<category_id>/delete', views.foodCategory_delete, name='foodCategory_delete'),
    path('category/<category_id>/manageItems', views.food_category_manage_item, name='food_category_manage_item'),
    path('item', views.foodItem_index, name='foodItem_index'),
    path('item/<id>/edit', views.foodItem_edit, name='foodItem_edit'),
    path('item/<id>/delete', views.foodItem_delete, name='foodItem_delete'),
]