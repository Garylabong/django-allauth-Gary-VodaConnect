from django import forms
from django.forms import ModelForm
from django.db.models import fields
from Billing.models import MonthlyCharge
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
            label = "Total Cost",
            widget=forms.TextInput(attrs={"class": "form-control6", "type": "number"}),
        )
        self.fields["month_covered"] = forms.DateField(
            required=True,
            label = "Month Covered",
            widget=forms.DateInput(attrs={"class": "form-control7", "type": "date"}),
        )
        self.fields["date_payment"] = forms.DateField(
            required=True,
            label = "Date Payment",
            widget=forms.DateInput(attrs={"class": "form-control8", "type": "date"}),
        )
        self.fields["reference"] = forms.CharField(
            required=True,
            label = "Reference",
            widget=forms.TextInput(attrs={"class": "form-control9"}),
        )
