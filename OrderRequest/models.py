from django.db import models
from authentication.models import *
from SubscribersInventory.models import *

# Create your models here.
class OrderRequest(models.Model):
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

    CATEGORY_REQUEST_CHOICES = (
        ("Connect to CallMe.Com.Ph", "Connect to CallMe.Com.Ph"),
        ("Connect to PsalmsGlobal", "Connect to PsalmsGlobal"),
        ("Personal Use", "Personal Use"),
        ("Business Use", "Business Use"),
        ("Others", "Others"),
    )
    ORDER_STATUS_CHOICES = (
        ("New Order", "New Order"),
        ("Pending Request", "Pending Request"),
        ("Processing", "Processing"),
        ("Follow-up with the Client", "Follow-up with the Client"),
        ("Declined", "Declined"),
        ("Order Complete", "Order Complete"),
    )

    date_request = models.DateField(null=True, blank=True)
    plan_type = models.CharField(
        max_length=150,
        choices=PLAN_CHOICES,
        null=True,
        blank=True,
        verbose_name="Type of Plan",
    )
    company_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="Company Name ( That will appear in your caller ID)",
    )
    address = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Complete Address ( Incase of porting)",
    )
    preferred_code = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="Prepared Area Code"
    )
    phone_number = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="total Number Of Phone Lines Needed",
    )
    fax = models.CharField(
        max_length=150,
        choices=FAX_CHOICES,
        null=True,
        blank=True,
        verbose_name="Do You Need Fax?",
    )
    request = models.CharField(
        max_length=150,
        choices=REQUEST_CHOICES,
        null=True,
        blank=True,
        verbose_name="Type Of Request",
    )
    category_request = models.CharField(
        max_length=150,
        choices=CATEGORY_REQUEST_CHOICES,
        null=True,
        blank=True,
        verbose_name="Category Of Request",
    )
    email = models.EmailField(
        null=True, blank=True, verbose_name="PayPal Email Address for Billing"
    )
    order_status = models.CharField(
        max_length=150,
        choices=ORDER_STATUS_CHOICES,
        null=True,
        blank=True,
        verbose_name="Order Status",
    )
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address
