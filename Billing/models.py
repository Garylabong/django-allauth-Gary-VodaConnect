from django.db import models
from authentication.models import *
from SubscribersInventory.models import *

# Create your models here.


class MonthlyCharge(models.Model):
    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("UnPaid", "UnPaid"),
    )
    client_full_name = models.ForeignKey(VOIPInformation, on_delete=models.CASCADE)
    client_code = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    vodaconnect_number = models.ForeignKey(VodaConnectNumber, on_delete=models.CASCADE)
    plan_types = models.ForeignKey(PlanType, on_delete=models.CASCADE)
    total_cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
        verbose_name="Total Cost",
    )
    month_covered = models.DateField(null=True, blank=True)
    date_payment = models.DateField(null=True, blank=True)
    reference = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(
        max_length=150, choices=STATUS_CHOICES, null=True, blank=True
    )

    class Meta:
        verbose_name = "Monthly Charges"
        verbose_name_plural = "Monthly Charges"
        ordering = ["reference"]

    def __str__(self):
        return self.reference


class OtherCharge(models.Model):
    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("UnPaid", "UnPaid"),
    )
    date = models.DateField(null=True, blank=True)
    vodaconnect_number = models.ForeignKey(VodaConnectNumber, on_delete=models.CASCADE)
    type_charge = models.CharField(max_length=250, null=True, blank=True)
    amount = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
        verbose_name="Amount",
    )
    pay_ref = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Payment Reference"
    )
    status = models.CharField(
        max_length=150, choices=STATUS_CHOICES, null=True, blank=True
    )
    notes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Other Charges"
        verbose_name_plural = "Other Charges"
        ordering = ["type_charge"]

    def __str__(self):
        return self.type_charge
