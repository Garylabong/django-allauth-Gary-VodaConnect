from django.db import models
from SubscribersInventory.models import VoIpInformation
from django import forms
from django.forms import ModelForm
from django.db.models import fields
from Billing.models import MonthlyCharge, OtherCharge
from SubscribersInventory.models import VoIpInformation
import datetime


class DateInput(forms.DateInput):
    input_type = "date"


class MonthlyChargeCreateForm(ModelForm):
    class Meta:
        model = MonthlyCharge
        fields = (
            "client_full_name",
            "client_code",
            "vodaconnect_number",
            "plan_type",
            "total_cost",
            "month_covered",
            "date_payment",
            "status",
            "reference",
        )

    def __init__(self, *args, **kwargs):
        super(MonthlyChargeCreateForm, self).__init__(*args, **kwargs)
        PLAN_CHOICES = (
            (
                "",
                "-----------",
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
        STATUS_CHOICES = (
            ("", "-------"),
            ("Paid", "Paid"),
            ("UnPaid", "UnPaid"),
        )
        self.fields["status"] = forms.ChoiceField(
            required=True,
            label="Status",
            choices=STATUS_CHOICES,
        )
        self.fields["plan_type"] = forms.ChoiceField(
            required=True,
            label="Plan Type",
            choices=PLAN_CHOICES,
        )
        self.fields["client_full_name"] = forms.CharField(
            required=True,
            label="Client Full Name",
            widget=forms.TextInput(
                attrs={"class": "form-control1", "placeholder": "Full Name"}
            ),
        )
        self.fields["client_code"] = forms.CharField(
            required=True,
            label="Client Code",
            widget=forms.TextInput(
                attrs={"class": "form-control1", "placeholder": "Code"}
            ),
        )
        self.fields["total_cost"] = forms.CharField(
            required=True,
            label="Total Cost",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control6",
                    "type": "number",
                    "placeholder": "00.00",
                }
            ),
        )
        self.fields["month_covered"] = forms.DateField(
            required=True,
            label="Month Covered",
            widget=forms.DateInput(attrs={"class": "form-control7", "type": "date"}),
        )
        self.fields["date_payment"] = forms.DateField(
            required=True,
            label="Date Payment",
            widget=forms.DateInput(attrs={"class": "form-control8", "type": "date"}),
        )
        self.fields["reference"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={"class": "form-control9", "placeholder": "Reference"}
            ),
        )


class MonthlyChargeUpdateForm(ModelForm):
    class Meta:
        model = MonthlyCharge

        fields = (
            "plan_type",
            "total_cost",
            "month_covered",
            "date_payment",
            "reference",
            "status",
        )

    def __init__(self, *args, **kwargs):
        super(MonthlyChargeUpdateForm, self).__init__(*args, **kwargs)
        PLAN_CHOICES = (
            (
                "",
                "-----------",
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
        self.fields["plan_type"] = forms.ChoiceField(
            required=True,
            label="Plan Type",
            choices=PLAN_CHOICES,
        )
        self.fields["total_cost"] = forms.CharField(
            required=True,
            disabled=True,
            label="Total Cost",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control5",
                    "type": "number",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["month_covered"] = forms.DateField(
            required=True,
            disabled=True,
            label="Month Covered",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control5",
                    "type": "date",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["date_payment"] = forms.DateField(
            required=True,
            disabled=True,
            label="Date Payment",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control5",
                    "type": "date",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["reference"] = forms.CharField(
            required=True,
            label="Reference",
            widget=forms.TextInput(attrs={"class": "form-control9"}),
        )
        self.fields["status"] = forms.CharField(
            required=True,
            disabled=True,
            label="Status",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control5",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )


class MonthlyChargeEditForm(ModelForm):
    class Meta:
        model = VoIpInformation
        fields = (
            "client_full_name",
            "client_code",
            "vodaconnect_number",
        )

    def __init__(self, *args, **kwargs):
        super(MonthlyChargeEditForm, self).__init__(*args, **kwargs)
        self.fields["client_full_name"] = forms.CharField(
            required=True,
            label="Client FullName",
            widget=forms.TextInput(attrs={"class": "form-control6"}),
        )


class OtherChargeCreateForm(ModelForm):
    class Meta:
        model = OtherCharge
        fields = (
            "date",
            "vodaconnect_number",
            "type_charge",
            "amount",
            "pay_ref",
            "status",
            "notes",
        )

    def __init__(self, *args, **kwargs):
        super(OtherChargeCreateForm, self).__init__(*args, **kwargs)
        STATUS_CHOICES = (
            ("", "-------"),
            ("Paid", "Paid"),
            ("UnPaid", "UnPaid"),
        )
        self.fields["date"] = forms.DateField(
            required=True,
            label="Date ",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control1",
                    "type": "date",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["type_charge"] = forms.CharField(
            required=True,
            label="Type Of Charge",
            widget=forms.TextInput(attrs={"class": "form-control2"}),
        )
        self.fields["amount"] = forms.IntegerField(
            required=True,
            label="Amount",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control3",
                    "type": "number",
                    "placeholder": "00.00",
                }
            ),
        )
        self.fields["pay_ref"] = forms.CharField(
            required=True,
            label="Payment Reference",
            widget=forms.TextInput(attrs={"class": "form-control4"}),
        )
        self.fields["status"] = forms.ChoiceField(
            required=True,
            label="Status",
            choices=STATUS_CHOICES,
        )
        self.fields["notes"] = forms.CharField(
            required=True,
            widget=forms.Textarea(
                attrs={"class": "form-control5", "placeholder": "Notes"}
            ),
        )


class OtherChargeUpdateForm(ModelForm):
    class Meta:
        model = OtherCharge
        fields = (
            "date",
            "vodaconnect_number",
            "type_charge",
            "amount",
            "pay_ref",
            "status",
            "notes",
        )

    def __init__(self, *args, **kwargs):
        super(OtherChargeUpdateForm, self).__init__(*args, **kwargs)
        STATUS_CHOICES = (
            ("", "-------"),
            ("Paid", "Paid"),
            ("UnPaid", "UnPaid"),
        )
        self.fields["date"] = forms.DateField(
            required=True,
            label="Date ",
            widget=forms.DateInput(
                attrs={
                    "class": "form-control1",
                    "type": "date",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["type_charge"] = forms.CharField(
            required=True,
            label="Type Of Charge",
            widget=forms.TextInput(attrs={"class": "form-control2"}),
        )
        self.fields["amount"] = forms.IntegerField(
            required=True,
            label="Amount",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control3",
                    "type": "number",
                    "placeholder": "00.00",
                }
            ),
        )
        self.fields["pay_ref"] = forms.CharField(
            required=True,
            label="Payment Reference",
            widget=forms.TextInput(attrs={"class": "form-control4"}),
        )
        self.fields["status"] = forms.ChoiceField(
            required=True,
            label="Status",
            choices=STATUS_CHOICES,
        )
        self.fields["notes"] = forms.CharField(
            required=True,
            widget=forms.Textarea(
                attrs={"class": "form-control5", "placeholder": "Notes"}
            ),
        )
