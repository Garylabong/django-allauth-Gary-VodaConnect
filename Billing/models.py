from django.db import models
from authentication.models import *
from SubscribersInventory.models import *

# Create your models here.


class MonthlyCharge(models.Model):
    PLAN_CHOICES = (
        (
            "BASIC PACKAGES/STANDARD/$4.99/MONTHLY",
            "BASIC PACKAGES/STANDARD/$4.99/MONTHLY",
        ),
        (
            "BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY",
            "BASIC PACKAGES/PROFESSIONAL/$19.95/MONTHLY",
        ),
        (
            "BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY",
            "BASIC PACKAGES/ENTERPRISE/$24.95/MONTHLY",
        ),
        (
            "12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY",
            "12-24 MOS. LOCK IN PLANS/STANDARD/$4.99/MONTHLY",
        ),
        (
            "12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY",
            "12-24 MOS. LOCK IN PLANS/PROFESSIONAL/$14.99/MONTHLY",
        ),
        (
            "12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY",
            "12-24 MOS. LOCK IN PLANS/ENTERPRISE/$19.99/MONTHLY",
        ),
        (
            "TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY",
            "TEXT AND CALL  FEATURES/STANDARD/$8.99/MONTHLY",
        ),
        (
            "TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY",
            "TEXT AND CALL  FEATURES/PROFESSIONAL/$21.99/MONTHLY",
        ),
        (
            "TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY",
            "TEXT AND CALL  FEATURES/ENTERPRISE/$29.99/MONTHLY",
        ),
        (
            "TEXT MESSAGING/Standard/$8.95/MONTHLY",
            "TEXT MESSAGING/Standard/$8.95/MONTHLY",
        ),
        (
            "TEXT MESSAGING/	Professional/$11.95/MONTHLY",
            "TEXT MESSAGING/	Professional/$11.95/MONTHLY",
        ),
        (
            "TEXT MESSAGING/	Enterprise/$14.95/MONTHLY",
            "TEXT MESSAGING/	Enterprise/$14.95/MONTHLY",
        ),
        (
            "TEXT MESSAGING/	Enterprise Plus (Volume Pricing)/$4.95 Access Fee",
            "TEXT MESSAGING/	Enterprise Plus (Volume Pricing)/$4.95 Access Fee",
        ),
        (
            "TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY",
            "TOLL-FREE/OPTION 1/1800-$29.95/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY",
            "TOLL-FREE/OPTION 1/1888-$29.95/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY",
            "TOLL-FREE/OPTION 1/1877-$29.95/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY",
            "TOLL-FREE/OPTION 1/1866-$29.95/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY",
            "TOLL-FREE/OPTION 2/1800-$9.99/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY",
            "TOLL-FREE/OPTION 2/1888-$9.99/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY",
            "TOLL-FREE/OPTION 2/1877-$12.99/MONTHLY",
        ),
        (
            "TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY",
            "TOLL-FREE/OPTION 2/1866-$12.99/MONTHLY",
        ),
        ("FAX NUMBER/FAX NUMBER/$7.99/MONTHLY", "FAX NUMBER/FAX NUMBER/$7.99/MONTHLY"),
        (
            "FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00",
            "FAX NUMBER/Porting/CAT A-$5.00,CAT C-$100.00",
        ),
        (
            "CORPORATE PACKAGES/STANDARD/$699/MONTHLY",
            "CORPORATE PACKAGES/STANDARD/$699/MONTHLY",
        ),
        (
            "CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY",
            "CORPORATE PACKAGES/PROFESSIONAL/$1299/MONTHLY",
        ),
        (
            "CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY",
            "CORPORATE PACKAGES/ENTERPRISE/$2899/MONTHLY",
        ),
        (
            "VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY",
            "VIDEO CONFERENCING/Hassle-Free Video Conferencing with WebRTC/$49 USD/MONTHLY",
        ),
        (
            "IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY",
            "IP-TV - INDIVIDUAL PACKAGES/SEE TV NETWORK/$4.99/ MONTHLY",
        ),
    )
    FAX_CHOICES = (("Yes", "Yes"), ("No", "No"))

    REQUEST_CHOICES = (
        ("New Number Request", "New Number Request"),
        ("Porting Request", "Porting Request"),
        ("Other Request", "Other Request"),
    )
    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("UnPaid", "UnPaid"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    client_full_name = models.ForeignKey(VoIpInformation, on_delete=models.CASCADE)
    client_code = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    vodaconnect_number = models.ForeignKey(VodaConnectNumber, on_delete=models.CASCADE)
    plan_type = models.CharField(
        max_length=150,
        choices=PLAN_CHOICES,
        null=True,
        blank=True,
        verbose_name="Type of Plan",
    )
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
