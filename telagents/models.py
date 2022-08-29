from django.db import models
from datetime import datetime
# from pytz import timezone
import decimal
from decimal import Decimal
from random import randint
from django.forms import ModelForm
from telagents.forms import AmountForm

class User(models.Model):
    access_card = models.IntegerField(primary_key=True, max_length=15)
    PIN = models.IntegerField(max_length=5 )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    client_since = models.DateTimeField('Client since')
    # bank_account = models.OneToMany(BankAccount, to_field='user', on_delete=models.CASCADE)

    def creation_date(self):
        # a = self.pub_date.timezone.now("US")
        # b = pytz.timezone("US")
        return self.client_since.strftime("%A %d %B %Y @ %I:%M:%S %p")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}'s bank account."
    
class BankAccount(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.IntegerField(primary_key=True, max_length=6)
    interest = models.DecimalField(max_digits=6, decimal_places=3) # Percent
    account_opened = models.DateTimeField('Inception date')
    transit_number = models.IntegerField(max_length=5)
    
    def __str__(self):
        return f"{self.transit_number} / {self.account_number}"

class Ledger(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    # bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=12, decimal_places=2)
    credit = models.DecimalField(max_digits=12, decimal_places=2)
    running_balance = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    trans_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    trans_id = models.BigIntegerField()

'''
    class Meta:
        model = Account
        fields = ['amount',]
 '''

'''
    account_num = randint(9999999,99999999)
    balance = round(Decimal(starting_balance),2)
    transaction_id = randint(101,999)
'''