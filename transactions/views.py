from django.shortcuts import render, redirect

from transactions.models import Transaction
from .forms import TransactionForm

# Create your views here.
def index(request,transactionId):
    transaction = Transaction.objects.get(pk=transactionId)
    transactionForm =TransactionForm(instance=transaction)
    if request.method == 'POST':
        transactionForm = TransactionForm(request.POST, instance=transaction)
        if transactionForm.is_valid():
            transactionForm.save()
            return redirect(f"/reservation/booking/{transaction.reservation.id}")
    return render(request,'transactions/editTransaction.html',{'transactionForm':transactionForm,'transactionId':transactionId})


def delete(request,transactionId):
    transaction = Transaction.objects.get(pk=transactionId)
    transaction.delete()
    return redirect(f"/reservation/booking/{transaction.reservation.id}")