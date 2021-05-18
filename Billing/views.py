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
)

from Billing.forms import MonthlyChargeCreateForm

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
    fields = "__all__"
    template_name = "Billing/monthlycharge_Update.html"
    success_url = reverse_lazy("bill:month_list")
