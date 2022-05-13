from django.db import models
from datetime import datetime
#from pytz import timezone
import decimal
from decimal import Decimal
from random import randint


class Account(models.Model):
    interest = models.DecimalField(max_digits=6, decimal_places=3) # Decimal('0.005') # Percent
    inception_date = models.DateTimeField('Client since (inception date)')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account_number = models.BigIntegerField()
    '''
    last_name = last_name
    full_name = f'{first_name} {last_name}'
    account_num = randint(9999999,99999999)
    balance = round(Decimal(starting_balance),2)
    transaction_id = randint(101,999)
    
    def transaction_time_stamp(self):
        # a = self.pub_date.timezone.now("US")
        b = self.inception_date.strftime("%A %d %B %Y @ %I:%M:%S %p")
        # c = pytz.timezone("US")
        return b
    '''
    def __str__(self):
        return f'{self.first_name} {self.last_name}'