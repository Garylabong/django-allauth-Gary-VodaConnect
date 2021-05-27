from Billing.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (
    UpdateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)

from Billing.forms import (
    MonthlyChargeCreateForm,
    MonthlyChargeUpdateForm,
    MonthlyChargeEditForm,
    OtherChargeCreateForm,
    OtherChargeUpdateForm,
)

# MONTHLY CHARGE
class MonthlyChargeList(LoginRequiredMixin, ListView):
    model = MonthlyCharge
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class MonthlyChargeDetail(LoginRequiredMixin, DetailView):
    model = MonthlyCharge
    context_object_name = "detail"
    template_name = "Billing/monthlycharge_detail.html"


class MonthlyChargeCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MonthlyCharge
    form_class = MonthlyChargeCreateForm
    success_url = reverse_lazy("bill:month_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MonthlyChargeCreate, self).form_valid(form)

    def form_valid(self, form):
        messages.success(self.request, "Monthly Charge Created Successfully.")
        return super().form_valid(form)


class MonthlyChargeUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MonthlyCharge
    form_class = MonthlyChargeUpdateForm
    template_name = "Billing/monthlycharge_Update.html"
    success_url = reverse_lazy("bill:month_list")

    def form_valid(self, form):
        messages.success(self.request, "Monthly Charge Updated Successfully.")
        return super().form_valid(form)


class MonthlyChargeEdit(LoginRequiredMixin, UpdateView):
    model = VoIpInformation
    form_class = MonthlyChargeEditForm
    template_name = "Billing/monthlycharge_Update.html"
    success_url = reverse_lazy("bill:month_list")


class MonthlyChargeDelete(LoginRequiredMixin, DeleteView):
    model = VoIpInformation
    context_object_name = "delete"
    template_name = "Billing/monthlycharge_delete.html"
    success_url = reverse_lazy("bill:month_list")


# OTHER CHARGE
class OtherChargeListView(LoginRequiredMixin, ListView):
    model = OtherCharge
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class OtherChargeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = OtherCharge
    form_class = OtherChargeCreateForm
    success_url = reverse_lazy("bill:othercharge_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(OtherChargeCreateView, self).form_valid(form)

    def form_valid(self, form):
        messages.success(self.request, "Charge Created Successfully.")
        return super().form_valid(form)


class OtherChargeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = OtherCharge
    form_class = OtherChargeUpdateForm
    template_name = "Billing/othercharge_update.html"
    success_url = reverse_lazy("bill:othercharge_list")

    def form_valid(self, form):
        messages.success(self.request, "Charge Updated Successfully.")
        return super().form_valid(form)
