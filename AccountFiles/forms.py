from django import forms
from django.forms import ModelForm
from django.db.models import fields
from AccountFiles.models import AccountFile
import datetime


class ClientFileForm(ModelForm):
    class Meta:
        model = AccountFile
        fields = (
            "client_code",
            "client_full_name",
            "file_name",
            "url",
            "file_description",
        )

    def __init__(self, *args, **kwargs):
        super(ClientFileForm, self).__init__(*args, **kwargs)
        self.fields["client_full_name"] = forms.CharField(
            required=True,
            label="Client Full Name",
            widget=forms.TextInput(attrs={"class": "form-control3"}),
        )
        self.fields["file_name"] = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={"class": "form-control1"}),
        )
        self.fields["url"] = forms.CharField(
            required=True,
            widget=forms.TextInput(attrs={"class": "form-control2"}),
        )
        self.fields["file_description"] = forms.CharField(
            required=True,
            widget=forms.Textarea(attrs={"class": "form-control5"}),
        )
