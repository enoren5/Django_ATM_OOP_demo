from django.shortcuts import render
from telagents.models import Account
# Create your views here.

def index(request):
    #context = Account(request)
    data = Account.objects.all().order_by('-inception_date')
    context = {'data':data}
    return render(request, "telagents/home.html", context)

'''
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
'''

