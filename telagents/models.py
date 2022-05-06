from django.db import models
from datetime import datetime
from pytz import timezone
import decimal
from decimal import Decimal
from random import randint


class TimeZone(models.Model):
    
    def __init__(self):
        # self.selection = int(input("Howdy! Make your time zone selection: \n 1: Los Angeles \n 2: London \n 3: Shanghai \n 4: Sydney \n 5: Rio de Janeiro \n"))
        self.locality = "Asia/Shanghai" # Shanghai ,}
        '''
            1: "US/Pacific", # Los Angeles
            2: "Europe/London", # London
            3: "Asia/Shanghai", # Shanghai 
            4: "Australia/Sydney", # Sydney
            5: "Brazil/East", # Rio de Janeiro
        }'''   
        self.tz = datetime.now(timezone(self.locality)) # [self.selection]
        self.readable_format = '%Y-%m-%d %H:%M:%S %Z%z'
        print(f'The date and time: {self.tz.strftime(self.readable_format)}')
        self.transaction_time_id_format = '%Y%m%d%H%M%S'
        print(f'The date and time condensed: {self.tz.strftime(self.transaction_time_id_format)}')
    
    def condensed(self):
       return f'{self.tz.strftime(self.transaction_time_id_format)}'

class Account(models.Model):
    
    interest = models.DecimalField(max_digits=6, decimal_places=3) # Decimal('0.005') # Percent

    def __init__(self, first_name='Winston', last_name='Smith', account_num=10000001, starting_balance=0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'
        self.account_num = randint(9999999,99999999)
        self.balance = round(Decimal(starting_balance),2)
        self.transaction_id = randint(101,999)
        self.tzone = TimeZone()
    
    def __str__(self):
        return (self.title)