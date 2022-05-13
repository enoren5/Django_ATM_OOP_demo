from django.db import models
from datetime import datetime
#from pytz import timezone
import decimal
from decimal import Decimal
from random import randint


class Account(models.Model):
    interest = models.DecimalField(max_digits=6, decimal_places=3) # Decimal('0.005') # Percent
    '''
    first_name = first_name
    last_name = last_name
    full_name = f'{first_name} {last_name}'
    account_num = randint(9999999,99999999)
    balance = round(Decimal(starting_balance),2)
    transaction_id = randint(101,999)
    '''
    def __str__(self):
        return (self.interest)