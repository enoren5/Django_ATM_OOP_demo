from datetime import datetime
from pytz import timezone
import decimal
from decimal import Decimal
from random import randint

class TimeZone:
    
    def __init__(self):
        self.selection = int(input("Howdy! Make your time zone selection: \n 1: Los Angeles \n 2: London \n 3: Shanghai \n 4: Sydney \n 5: Rio de Janeiro \n"))
        self.locality = {
            1: "US/Pacific", # Los Angeles
            2: "Europe/London", # London
            3: "Asia/Shanghai", # Shanghai 
            4: "Australia/Sydney", # Sydney
            5: "Brazil/East", # Rio de Janeiro
        }   
        self.tz = datetime.now(timezone(self.locality[self.selection]))
        self.readable_format = '%Y-%m-%d %H:%M:%S %Z%z'
        print(f'The date and time: {self.tz.strftime(self.readable_format)}')
        self.transaction_time_id_format = '%Y%m%d%H%M%S'
        print(f'The date and time condensed: {self.tz.strftime(self.transaction_time_id_format)}')
    
    def condensed(self):
       return f'{self.tz.strftime(self.transaction_time_id_format)}'

class Account:
    
    interest = Decimal('0.005') # Percen t

    def __init__(self, first_name, last_name, account_num=10000001, starting_balance=0.00):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f'{first_name} {last_name}'
        self.account_num = randint(9999999,99999999)
        self.balance = round(Decimal(starting_balance),2)
        self.transaction_id = randint(101,999)
        self.tzone = TimeZone()

    def deposit(self, amount):
        self.balance += round(Decimal(amount),2)
        self.transaction_id += randint(101,999) - randint(101,999) 
        return f'D-{self.account_num}-{self.tzone.condensed()}-{self.transaction_id}'
    
    def withdraw(self, amount):
        if amount > self.balance:         
            self.transaction_id += randint(101,999) - randint(101,999) 
            print(f'X-{self.account_num}-{self.tzone.condensed()}-{self.transaction_id}') 
            raise ValueError('Transaction declined. Insufficient funds. Please deposit some more $$$ first.')
            
        self.balance -= round(Decimal(amount),2)
        self.transaction_id += randint(101,999) - randint(101,999) 
        return f'W-{self.account_num}-{self.tzone.condensed()}-{self.transaction_id}'

    def pay_interest(self):
        monthly_rate = self.interest/12
        monthly_sum = monthly_rate * self.balance
        self.transaction_id += randint(101,999) - randint(101,999) 
        print(f'I-{self.account_num}-{self.tzone.condensed()}-{self.transaction_id}') 
        return round(Decimal(monthly_sum, + self.balance), 2)

    def __repr__(self):
        """Return a string that represents the account."""
        return f"{self.__class__.__name__}({self.last_name}, {self.first_name}, balance={self.balance})"
'''
if __name__ == "__main__":
    selection = int(input(" Howdy! Make your time zone selection: \n 1: Los Angeles \n 2: London \n 3: Shanghai \n 4: Sydney \n 5: Rio de Janeiro \n"))
    locality = {
        1: "US/Pacific", # Los Angeles,
        2: "Europe/London'", # London, 
        3: "Asia/Shanghai", # Shanghai, 
        4: "Australia/Sydney", # Sydney, 
        5: "Brazil/East", # Rio de Janeiro
    }
'''