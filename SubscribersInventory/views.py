from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import ActivationDetailForm, PlanDetailsUpdateForm
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.views import View
from .views import *
from .models import *


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "SubscribersInventory/home.html"


class SubsInvView(LoginRequiredMixin, TemplateView):
    template_name = "SubscribersInventory/subs_inventory.html"


# vOIPiNFO
class VoipListView(LoginRequiredMixin, ListView):
    model = VoIpInformation
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class VoipDetailView(DetailView):
    model = VoIpInformation
    context_object_name = "detail"
    template_name = "SubscribersInventory/voipinformation_detail.html"


# ACTIVATION DETAILS
class ActivationDetailListView(LoginRequiredMixin, ListView):
    model = ActivationDetail
    context_object_name = "list"
    template_name = "SubscribersInventory/activationdetail_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class ActivationDetailAddView(SuccessMessageMixin, CreateView):
    model = ActivationDetail
    form_class = ActivationDetailForm
    context_object_name = "add"
    template_name = "SubscribersInventory/activationdetails_addview.html"
    success_message = "%(activationdetail)s created successfully"

    def form_valid(self, form):
        activationdetail = form.save(commit=False)
        activationdetail.user = self.request.user
        activationdetail.save()
        messages.success(self.request, "✔ You have been Created a Details.")
        return redirect("subs_Inv:activation_details_list")


# PLAN DETAILS
class PlanDetailsListView(LoginRequiredMixin, ListView):
    model = PlanDetail
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class PlanDetailsUpdateView(LoginRequiredMixin, UpdateView):
    model = PlanDetail
    form_class = PlanDetailsUpdateForm
    template_name = "SubscribersInventory/plandetail_form.html"
    success_url = reverse_lazy("subs_Inv:plan_details")

    def form_valid(self, form):
        messages.success(self.request, " ✔ Plan Details updated successfully.")
        return super().form_valid(form)


# SUBSCRIBER STATUS
class SubscribersStatusListView(LoginRequiredMixin, ListView):
    model = SubscriberStatus
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class SubscribersStatusUpdateView(LoginRequiredMixin, UpdateView):
    model = SubscriberStatus
    fields = ["stat_production", "type_of_request", "ready_for_testimony"]
    template_name = "SubscribersInventory/subscriberstatus_form.html"
    success_url = reverse_lazy("subs_Inv:plan_details")

    def form_valid(self, form):
        messages.success(self.request, " ✔ Status Updated Successfully.")
        return super().form_valid(form)


# FORWARDING INFORMATION
class ForwardingInfoListView(LoginRequiredMixin, ListView):
    model = ForwardingInfo
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context
