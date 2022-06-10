from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import BankAccount, User, Transaction
# Create your views here.
from .forms import AmountForm

def index(request):
    # Starting balance variable initialization:
    balance = 0 
    context = {'balance': balance}
    # Import `Account` model data:
    data1 = User.objects.all()
    data2 = BankAccount.objects.all()
    myaccount = Transaction.objects.get(id=1)
    # If this is a POST request we need to process the form data:
    print(request.POST)
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = AmountForm(request.POST)
        # Check whether it's valid:
        if form.is_valid():
            # Process the data in form.cleaned_data as required:
            amount = form.cleaned_data['amount']
            if request.POST['transaction'] == 'Deposit':
                balance = balance + amount
                context.update({'balance': balance,})
            if request.POST['transaction'] == 'Withdraw':
                balance = balance - amount
                context.update({'balance': balance,})
            myaccount.balance = balance
            myaccount.save()
            return render(request, 'telagents/home.html', {'form': form, 'data1':data1, 'data2':data2, 'context': context,})

    # If a GET (or any other method) we'll create a blank form:
    else:
        form = AmountForm()

    return render(request, 'telagents/home.html', {'form': form, 'data':data, })

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

