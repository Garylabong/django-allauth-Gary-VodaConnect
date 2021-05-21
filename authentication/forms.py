from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.forms import ModelForm
from django.db.models import fields
from AccountFiles.models import AccountFile
from authentication.models import User, Client
from django.db import transaction
import datetime


class MyCustomLoginForm(LoginForm):
    class Meta:
        model = User
        fields = ("password",)

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["password"] = forms.CharField(
            required=True,
            label="",
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control2",
                    "type": "password",
                    "placeholder": "Password",
                }
            ),
        )


class MyCustomSignupForm(SignupForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "last_name",
            "email",
            "phone_number",
            "create_pin",
            "password1",
            "password2",
            "company_name",
            "designation_name",
        )

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        DESIGNATION_CATEGORY = (
            ("", "Select your Designation"),
            ("Staff", "Staff"),
            ("New Client", "New Client"),
            ("Current Client", "Current Client"),
            ("Affiliate Partner", "Affiliate Partner"),
        )
        COMPANY_CATEGORY = (
            ("", "Select your Company"),
            ("Vodaconnect", "Vodaconnect"),
            ("G.P.G Corporation", "G.P.G Corporation"),
            ("Landmaster.Us", "Landmaster.Us"),
            ("CallMe.Com.Ph", "CallMe.Com.Ph"),
            ("PsalmsGlobal.Com", "PsalmsGlobal.Com"),
            ("Affiliate Partner", "Affiliate Partner"),
        )
        self.fields["first_name"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={"class": "form-control1", "placeholder": "First Name"}
            ),
        )
        self.fields["last_name"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={"class": "form-control2", "placeholder": "Last Name"}
            ),
        )
        self.fields["email"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control3",
                    "type": "email",
                    "placeholder": "Email",
                }
            ),
        )
        self.fields["username"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={"class": "form-control4", "placeholder": "Username"}
            ),
        )
        self.fields["phone_number"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control5",
                    "type": "number",
                    "placeholder": "Phone Number",
                }
            ),
        )
        self.fields["create_pin"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control6",
                    "type": "number",
                    "placeholder": "Create Pin",
                }
            ),
        )
        self.fields["password1"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control7",
                    "type": "password",
                    "placeholder": "Password",
                }
            ),
        )
        self.fields["password2"] = forms.CharField(
            required=True,
            label="",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control8",
                    "type": "password",
                    "placeholder": "Confirm Password",
                }
            ),
        )
        self.fields["company_name"] = forms.ChoiceField(
            required=True,
            label="",
            choices=COMPANY_CATEGORY,
        )
        self.fields["designation_name"] = forms.ChoiceField(
            required=True,
            label="",
            choices=DESIGNATION_CATEGORY,
        )

    @transaction.atomic
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.phone_number = self.cleaned_data.get("phone_number")
        user.create_pin = self.cleaned_data.get("create_pin")
        user.company_name = self.cleaned_data.get("company_name")
        user.designation_name = self.cleaned_data.get("designation_name")
        user.email = self.cleaned_data.get("email")
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.first_name = self.cleaned_data.get("first_name")
        client.last_name = self.cleaned_data.get("last_name")
        client.phone_number = self.cleaned_data.get("phone_number")
        client.email = self.cleaned_data.get("email")
        client.create_pin = self.cleaned_data.get("create_pin")
        client.company_name = self.cleaned_data.get("company_name")
        client.designation_name = self.cleaned_data.get("designation_name")
        client.save()
        return user


class ClientEditForm(ModelForm):
    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "create_pin",
        )

    def __init__(self, *args, **kwargs):
        super(ClientEditForm, self).__init__(*args, **kwargs)
        self.fields["username"] = forms.CharField(
            required=True,
            disabled=True,
            label="Username",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control1",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["first_name"] = forms.CharField(
            required=True,
            label="First Name",
            widget=forms.TextInput(attrs={"class": "form-control12"}),
        )
        self.fields["last_name"] = forms.CharField(
            required=True,
            label="Last Name",
            widget=forms.TextInput(attrs={"class": "form-control3"}),
        )
        self.fields["phone_number"] = forms.CharField(
            required=True,
            label="Phone Number",
            widget=forms.TextInput(attrs={"class": "form-control4", "type": "number"}),
        )
        self.fields["email"] = forms.CharField(
            required=True,
            disabled=True,
            label="Email Address",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control5",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["create_pin"] = forms.CharField(
            required=True,
            disabled=True,
            label="Create Pin",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control6",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )


class ClientEditInfoForm(ModelForm):
    class Meta:
        model = Client
        fields = (
            "affiliate_partner_code",
            "affiliate_partner_name",
            "company_name",
            "designation_name",
            # "lead_information",
            "profile_picture",
        )

    def __init__(self, *args, **kwargs):
        super(ClientEditInfoForm, self).__init__(*args, **kwargs)
        self.fields["company_name"] = forms.CharField(
            required=True,
            disabled=True,
            label="Company",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control1",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["designation_name"] = forms.CharField(
            required=True,
            disabled=True,
            label="Designation",
            widget=forms.TextInput(
                attrs={
                    "class": "form-control2",
                    "style": "background-color: transparent",
                    "border-color": "#ed5fdc",
                }
            ),
        )
        self.fields["affiliate_partner_code"] = forms.CharField(
            required=False,
            label="Affiliate Partner Code",
            widget=forms.TextInput(attrs={"class": "form-control3"}),
        )
        self.fields["affiliate_partner_name"] = forms.CharField(
            required=False,
            label="Affiliate Partner Name",
            widget=forms.TextInput(attrs={"class": "form-control4"}),
        )
        # self.fields["lead_information"] = forms.CharField(
        #     required=True,
        #     label="Lead Information",
        #     widget=forms.Textarea(attrs={"class": "form-control5"}),
        # )


class ClientAddForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "profile_picture",
            "pin",
            "company_name",
            "designation_name",
        )


class ClientFileForm(ModelForm):
    class Meta:
        model = AccountFile
        fields = (
            "file_name",
            "url",
            "file_description",
        )

    def __init__(self, *args, **kwargs):
        super(ClientFileForm, self).__init__(*args, **kwargs)
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
