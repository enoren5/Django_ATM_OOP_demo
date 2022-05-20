from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Account
# Create your views here.
from .forms import AmountForm

def index(request):
    balance = 0
    data = Account.objects.all().order_by('-inception_date')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AmountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            deposit = form.cleaned_data['deposit']
            withdraw = form.cleaned_data['withdraw']
            amount = form.cleaned_data['amount']
            context = {'balance': balance}
            if deposit:
                balance = balance + amount
                context.update({'balance': balance,})
            elif withdraw:
                balance = balance - withdraw
                context.update({'balance': balance,})
            # redirect to a new URL:
            return render(request, 'telagents/home.html', {'form': form, 'data':data, 'context': context,})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AmountForm()

    return render(request, 'telagents/home.html', {'form': form, 'data':data,})

''' def process_transaction(request):
    return HttpResponse('You are on the process transaction page')

context = Account(request)
    balances = 0
    withdrawals = 0
    deposits = 0
    amounts = 0
    
    context = {'data':data,'withdrawals':withdrawals,'deposits':deposits,'amount':amounts, 'balances': balances,} # initialize context var to be updated after math operations
    return render(request, "telagents/home.html", context)


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

