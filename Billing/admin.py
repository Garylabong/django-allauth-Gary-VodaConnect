from django.contrib import admin
from Billing.models import MonthlyCharge, OtherCharge

# Register your models here.

admin.site.register(MonthlyCharge)
admin.site.register(OtherCharge)
