from django.db import models
from datetime import datetime
# from pytz import timezone
import decimal
from decimal import Decimal
from random import randint
from django.forms import ModelForm
from telagents.forms import AmountForm

class Account(models.Model):
    #### Static data elements :
    interest = models.DecimalField(max_digits=6, decimal_places=3) # Percent
    inception_date = models.DateTimeField('Client since (inception date)')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account_number = models.BigIntegerField()
    #### Interactive and dynamic data points :
    debit = models.DecimalField(max_digits=12, decimal_places=2)
    credit = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    trans_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    trans_id = models.BigIntegerField()

    def client_since(self):
        # a = self.pub_date.timezone.now("US")
        # b = pytz.timezone("US")
        return self.inception_date.strftime("%A %d %B %Y @ %I:%M:%S %p")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}'s bank account."
'''
class Transactions(ModelForm):
    class Meta:
        model = AmountForm
        fields = ['debit', 'credit', 'balance', 'amount',]
'''     


'''
    account_num = randint(9999999,99999999)
    balance = round(Decimal(starting_balance),2)
    transaction_id = randint(101,999)
'''