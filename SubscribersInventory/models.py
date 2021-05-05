from django.db import models
from authentication.models import *

# Create your models here.
class VodaConnectNumber(models.Model):
    vodaconnect_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.vodaconnect_number


class VOIPInformation(models.Model):
    vodaconnect_number = models.ForeignKey(VodaConnectNumber, on_delete=models.CASCADE)
    client_full_name = models.CharField(max_length=500, null=True, blank=True)
    client_code = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    company_name = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "VOIP Information"
        verbose_name_plural = "VOIP Information"
        ordering = ["client_full_name"]

    def __str__(self):
        return self.client_full_name


class ActivationDetail(models.Model):
    PHONE_LINE_STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Cancelled", "Cancelled"),
        ("Pending", "Pending"),
    )
    CLIENT_COMPANY_USER_CATEGORY = (
        ("Vodaconnect", "Vodaconnect"),
        # ('G.P.G Corporation', 'G.P.G Corporation'),
        ("Landmaster.Us", "Landmaster.Us"),
        ("CallMe.Com.Ph", "CallMe.Com.Ph"),
        ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
    )
    order_request_date = models.DateField(null=True, blank=True)
    request_date_initiated = models.DateField(null=True, blank=True)
    date_line_activated = models.DateField(null=True, blank=True)
    date_line_terminated = models.DateField(null=True, blank=True)
    phone_line_status = models.CharField(
        max_length=100, choices=PHONE_LINE_STATUS_CHOICES
    )
    client_company_user = models.CharField(
        max_length=150, choices=CLIENT_COMPANY_USER_CATEGORY, null=True, blank=True
    )

    class Meta:
        verbose_name = "Activation Details"
        verbose_name_plural = "Activation Details"
        ordering = ["client_company_user"]

    def __str__(self):
        return self.client_company_user


class PlanType(models.Model):
    plan_types = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.plan_types


class PlanDetail(models.Model):
    RECURRING_BILL_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
        ("Cancelled", "Cancelled"),
        ("Pending", "Pending"),
    )
    plan_types = models.ForeignKey(PlanType, on_delete=models.CASCADE)
    total_cost = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.00,
        null=True,
        blank=True,
        verbose_name="Total Cost",
    )
    recurring_bill = models.CharField(
        max_length=100,
        choices=RECURRING_BILL_CHOICES,
        verbose_name="Did we set up recurring bill?",
    )
    pypal_bill = models.TextField(
        null=True, blank=True, verbose_name="Paypal Details for Billing"
    )
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Plan Details"
        verbose_name_plural = "Plan Details"
        ordering = ["pypal_bill"]

    def __str__(self):
        return self.pypal_bill


class SubscriberStatus(models.Model):
    STATUS_IN_PRODUCTION = (
        ("New Prospect", "New Prospect"),
        ("New Request", "New Request"),
        ("Pending Request", "Pending Request"),
        ("Call/Email Follow up", "Call/Email Follow up"),
        ("Ready to Start", "Ready to Start"),
        ("Sign up - Ready for Set up", "PendSign up - Ready for Set uping"),
        ("Active - Live in Production", "Active - Live in Production"),
        ("Request for Cancellation", "Request for Cancellation"),
        ("Email sent for Cancellation", "Email sent for Cancellation"),
        ("Account Cancelled by Vodaconnect", "Account Cancelled by Vodaconnect"),
        ("Recurring Charge Cancelled", "Recurring Charge Cancelled"),
        ("Account Cancelled", "Account Cancelled"),
    )
    TYPE_OF_REQUEST_CHOICES = (
        ("New Number Request", "New Number Request"),
        ("Porting Request", "Porting Request"),
        ("Other Request", "Other Request"),
    )
    TESTIMONY_CHOICES = (
        ("Yes", "Yes"),
        ("No", "No"),
        ("Not Applicable", "Not Applicable"),
    )
    stat_production = models.CharField(
        max_length=100,
        choices=STATUS_IN_PRODUCTION,
        verbose_name="Status In Production",
    )
    type_of_request = models.CharField(
        max_length=100, choices=TYPE_OF_REQUEST_CHOICES, verbose_name="Type of Request "
    )
    ready_for_testimony = models.CharField(
        max_length=100, choices=TESTIMONY_CHOICES, verbose_name="Ready For Testimony?"
    )

    class Meta:
        verbose_name = "Subscriber Status"
        verbose_name_plural = "Subscriber Status"
        ordering = ["stat_production"]

    def __str__(self):
        return self.stat_production


class ForwardingInfo(models.Model):
    forwarding_num = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Forwarding Number: (Customer Phone Line)",
    )

    class Meta:
        verbose_name = "Forwarding Information"
        verbose_name_plural = "Forwarding Information"
        ordering = ["forwarding_num"]

    def __str__(self):
        return self.forwarding_num


class TotalNumExtension(models.Model):
    extension_num = models.ForeignKey(
        ForwardingInfo, on_delete=models.CASCADE, verbose_name="Extension Number"
    )
    extension_logins = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.extension_logins


class ZiptrunkLoginDetail(models.Model):
    ziptrunk_logins = models.CharField(max_length=100, null=True, blank=True)
    ziptrunk_details = models.TextField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.ziptrunk_logins


class OtherLogin(models.Model):
    other_logins = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.other_logins


class Note(models.Model):
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.notes
