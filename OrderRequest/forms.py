from django import forms
from django.forms import ModelForm
from django.db.models import fields
from .models import OrderRequest
from django.db import transaction
import datetime


class DateInput(forms.DateInput):
    input_type = "date"


class OrderRequestForm(ModelForm):
    class Meta:
        model = OrderRequest
        fields = (
            "date_request",
            "plan_type",
            "company_name",
            "address",
            "preferred_code",
            "phone_number",
            "fax",
            "request",
            "category_request",
            "email",
            "order_status",
            "notes",
        )

    def __init__(self, *args, **kwargs):
        super(OrderRequestForm, self).__init__(*args, **kwargs)
        PLAN_CHOICES = (
            (
                "",
                "-------",
            ),
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
            (
                "FAX NUMBER/FAX NUMBER/$7.99/MONTHLY",
                "FAX NUMBER/FAX NUMBER/$7.99/MONTHLY",
            ),
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
        FAX_CHOICES = (("", "------"), ("Yes", "Yes"), ("No", "No"))

        REQUEST_CHOICES = (
            ("", "-------"),
            ("New Number Request", "New Number Request"),
            ("Porting Request", "Porting Request"),
            ("Other Request", "Other Request"),
        )

        CATEGORY_REQUEST_CHOICES = (
            ("", "------"),
            ("Connect to CallMe.Com.Ph", "Connect to CallMe.Com.Ph"),
            ("Connect to PsalmsGlobal", "Connect to PsalmsGlobal"),
            ("Personal Use", "Personal Use"),
            ("Business Use", "Business Use"),
            ("Others", "Others"),
        )
        ORDER_STATUS_CHOICES = (
            ("", "-------"),
            ("New Order", "New Order"),
            ("Pending Request", "Pending Request"),
            ("Processing", "Processing"),
            ("Follow-up with the Client", "Follow-up with the Client"),
            ("Declined", "Declined"),
            ("Order Complete", "Order Complete"),
        )
        COMPANY_CATEGORY = (
            ("", "-------"),
            ("Vodaconnect", "Vodaconnect"),
            ("G.P.G Corporation", "G.P.G Corporation"),
            ("Landmaster.Us", "Landmaster.Us"),
            ("CallMe.Com.Ph", "CallMe.Com.Ph"),
            ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
            ("Affiliate Partner", "Affiliate Partner"),
        )
        self.fields["date_request"] = forms.DateField(
            required=True,
            label="Date Request",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control1",
                    "placeholder": "Date request",
                    "type": "date",
                }
            ),
        )

        self.fields["plan_type"] = forms.ChoiceField(
            required=True,
            label="Plan Type",
            choices=PLAN_CHOICES,
        )
        self.fields["company_name"] = forms.ChoiceField(
            required=True,
            label="Company Name",
            choices=COMPANY_CATEGORY,
        )
        self.fields["address"] = forms.CharField(
            required=True,
            label="Complete Address",
            widget=forms.TextInput(
                attrs={"class": "form-control3", "placeholder": "Complete Address"}
            ),
        )

        self.fields["preferred_code"] = forms.CharField(
            required=True,
            label="Prepared Area Code",
            widget=forms.TextInput(
                attrs={"class": "form-control4", "placeholder": "Code"}
            ),
        )
        self.fields["phone_number"] = forms.CharField(
            required=True,
            label="Number Of Phone Lines Needed",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control5",
                    "type": "number",
                    "placeholder": "Input Number",
                }
            ),
        )
        self.fields["fax"] = forms.ChoiceField(
            required=True,
            label="Do You Need Fax?",
            choices=FAX_CHOICES,
        )
        self.fields["request"] = forms.ChoiceField(
            required=True,
            label="Type Of Request",
            choices=REQUEST_CHOICES,
        )
        self.fields["category_request"] = forms.ChoiceField(
            required=True,
            label="Category Of Request",
            choices=CATEGORY_REQUEST_CHOICES,
        )
        self.fields["email"] = forms.EmailField(
            required=True,
            label="Email",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "email",
                    "placeholder": "PayPal Email Address for Billing",
                    "style": "border-color: #ed5fdc;",
                }
            ),
        )
        self.fields["order_status"] = forms.ChoiceField(
            required=True,
            label="Order Status",
            choices=ORDER_STATUS_CHOICES,
        )
        self.fields["notes"] = forms.CharField(
            required=True,
            label="Notes",
            widget=forms.Textarea(
                attrs={
                    "class": "form-control2",
                    "placeholder": "Notes",
                    "style": "color: #0da34b;",
                }
            ),
        )
