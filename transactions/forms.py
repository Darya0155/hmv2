from django import forms

from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class AddOnTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('quantity','details')
