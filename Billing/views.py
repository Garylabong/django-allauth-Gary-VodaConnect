from re import M
from typing import List
from django.db.models import fields
from django.shortcuts import render
from Billing.models import *
from django.urls import reverse_lazy
from django.views.generic import (
    UpdateView,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
    DeleteView,
)

from Billing.forms import (
    MonthlyChargeCreateForm,
    MonthlyChargeUpdateForm,
    MonthlyChargeEditForm,
)


class MonthlyChargeList(ListView):
    model = MonthlyCharge
    context_object_name = "list"


class MonthlyChargeDetail(DetailView):
    model = MonthlyCharge
    context_object_name = "detail"
    template_name = "Billing/monthlycharge_detail.html"


class MonthlyChargeCreate(CreateView):
    model = MonthlyCharge
    form_class = MonthlyChargeCreateForm
    success_url = reverse_lazy("bill:month_list")


class MonthlyChargeUpdate(UpdateView):
    model = MonthlyCharge
    form_class = MonthlyChargeUpdateForm
    template_name = "Billing/monthlycharge_Update.html"
    success_url = reverse_lazy("bill:month_list")


class MonthlyChargeEdit(UpdateView):
    model = VoIpInformation
    form_class = MonthlyChargeEditForm
    template_name = "Billing/monthlycharge_Update.html"
    success_url = reverse_lazy("bill:month_list")


class MonthlyChargeDelete(DeleteView):
    model = VoIpInformation
    context_object_name = "delete"
    template_name = "Billing/monthlycharge_delete.html"
    success_url = reverse_lazy("bill:month_list")
