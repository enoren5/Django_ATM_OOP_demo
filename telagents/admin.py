from django.contrib import admin
from .models import User, BankAccount, Transaction #, TimeZone
# Register your models here.
admin.site.register(User)
admin.site.register(BankAccount)
admin.site.register(Transaction)
# admin.site.register(TimeZone)