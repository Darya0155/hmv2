from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path('logout/', views.user_logout, name='logout'),
    path("change-password/", views.change_password, name="change_password"),
]