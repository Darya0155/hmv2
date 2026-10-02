from django.urls import path
from . import views

urlpatterns = [
    path('<transactionId>/edit', views.index, name='edit_transaction_view'),
    path('<transactionId>/delete', views.delete, name='delete_transaction_view'),

]