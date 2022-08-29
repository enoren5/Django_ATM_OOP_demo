from django.contrib import admin
from .models import User, BankAccount, Ledger #, TimeZone
# Register your models here.
admin.site.register(User)
admin.site.register(BankAccount)
admin.site.register(Ledger)
# admin.site.register(TimeZone)