from django import forms
from django.forms import ModelForm

from .models import ActivationDetail


class DateInput(forms.DateInput):
    input_type = "date"


class ActivationDetailForm(forms.ModelForm):
    class Meta:
        model = ActivationDetail
        fields = (
            "order_request_date",
            "request_date_initiated",
            "date_line_activated",
            "date_line_terminated",
            "phone_line_status",
            "client_company_user",
        )
        widgets = {
            "order_request_date": DateInput(),
            "request_date_initiated": DateInput(),
            "date_line_activated": DateInput(),
            "date_line_terminated": DateInput(),
        }
