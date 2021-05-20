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

    def __init__(self, *args, **kwargs):
        super(ActivationDetailForm, self).__init__(*args, **kwargs)
        CLIENT_COMPANY_USER_CATEGORY = (
            ("", "-------"),
            ("Vodaconnect", "Vodaconnect"),
            ("Landmaster.Us", "Landmaster.Us"),
            ("CallMe.Com.Ph", "CallMe.Com.Ph"),
            ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
        )
        self.fields["client_company_user"] = forms.ChoiceField(
            required=True,
            label="Client Company User",
            choices=CLIENT_COMPANY_USER_CATEGORY,
        )
