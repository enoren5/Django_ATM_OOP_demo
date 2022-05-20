from django import forms

class AmountForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=6, decimal_places=2)
    