from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    DESIGNATION_CATEGORY = (
        ("Staff", "Staff"),
        ("New Client", "New Client"),
        ("Current Client", "Current Client"),
        ("Affiliate Partner", "Affiliate Partner"),
    )
    COMPANY_CATEGORY = (
        ("Vodaconnect", "Vodaconnect"),
        ("G.P.G Corporation", "G.P.G Corporation"),
        ("Landmaster.Us", "Landmaster.Us"),
        ("CallMe.Com.Ph", "CallMe.Com.Ph"),
        ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
        ("Affiliate Partner", "Affiliate Partner"),
    )
    is_client = models.BooleanField(default=False)
    is_staffs = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    create_pin = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(
        max_length=150, choices=COMPANY_CATEGORY, null=True, blank=True
    )
    designation_name = models.CharField(
        max_length=150, choices=DESIGNATION_CATEGORY, null=True, blank=True
    )

    def __str__(self):
        return self.username


class Client(models.Model):
    DESIGNATION_CATEGORY = (
        ("Staff", "Staff"),
        ("New Client", "New Client"),
        ("Current Client", "Current Client"),
        ("Affiliate Partner", "Affiliate Partner"),
    )
    COMPANY_CATEGORY = (
        ("Vodaconnect", "Vodaconnect"),
        ("G.P.G Corporation", "G.P.G Corporation"),
        ("Landmaster.Us", "Landmaster.Us"),
        ("CallMe.Com.Ph", "CallMe.Com.Ph"),
        ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
        ("Affiliate Partner", "Affiliate Partner"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    affiliate_partner_code = models.CharField(max_length=100, null=True, blank=True)
    affiliate_partner_name = models.CharField(max_length=100, null=True, blank=True)
    pin = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(
        max_length=150, choices=COMPANY_CATEGORY, null=True, blank=True
    )
    designation_name = models.CharField(
        max_length=150, choices=DESIGNATION_CATEGORY, null=True, blank=True
    )
    lead_information = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class ClientCode(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    client_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.client_code


class ClientPersonalFile(models.Model):
    client = models.ForeignKey(ClientCode, on_delete=models.CASCADE)
    file_title = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_title
