from django import forms

class AmountForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    #deposit = forms.DecimalField(label='Deposit', max_digits=10, decimal_places=2)
    # withdraw = forms.DecimalField(label='Withdraw', max_digits=10, decimal_places=2)

