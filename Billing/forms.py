from django.db import models
from SubscribersInventory.models import VoIpInformation
from django import forms
from django.forms import ModelForm
from django.db.models import fields
from Billing.models import MonthlyCharge
from SubscribersInventory.models import VoIpInformation
import datetime


class DateInput(forms.DateInput):
    input_type = "date"


class MonthlyChargeCreateForm(ModelForm):
    class Meta:
        model = MonthlyCharge

        fields = (
            "user",
            "client_full_name",
            "client_code",
            "vodaconnect_number",
            "plan_type",
            "total_cost",
            "month_covered",
            "date_payment",
            "reference",
            "status",
        )

    def __init__(self, *args, **kwargs):
        super(MonthlyChargeCreateForm, self).__init__(*args, **kwargs)
        self.fields["total_cost"] = forms.CharField(
            required=True,
            label="Total Cost",
            widget=forms.TextInput(attrs={"class": "form-control6", "type": "number"}),
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
            label="Reference",
            widget=forms.TextInput(attrs={"class": "form-control9"}),
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
