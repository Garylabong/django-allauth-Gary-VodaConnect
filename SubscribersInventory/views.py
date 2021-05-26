from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import (
    ActivationDetailForm,
    PlanDetailsUpdateForm,
    ForwardingInfoCreateForm,
    TotalNumExtensionCreateForm,
    ZiptrunkLoginDetailCreateForm,
    OtherLoginCreateForm,
    NoteCreateForm,
    ForwardingInfoUpdateForm,
    TotalNumExtensionUpdateForm,
    ZiptrunkLoginDetailUpdateForm,
    OtherLoginUpdateForm,
    NoteUpdateForm,
)
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


class ActivationDetailAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ActivationDetail
    form_class = ActivationDetailForm
    context_object_name = "add"
    template_name = "SubscribersInventory/activationdetails_addview.html"
    success_message = "%(activationdetail)s created successfully"

    def form_valid(self, form):
        activationdetail = form.save(commit=False)
        activationdetail.user = self.request.user
        activationdetail.save()
        messages.success(self.request, "You have been Created a Details.")
        return redirect("subs_Inv:activation_details_list")


# PLAN DETAILS
class PlanDetailsListView(LoginRequiredMixin, ListView):
    model = PlanDetail
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class PlanDetailsUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PlanDetail
    form_class = PlanDetailsUpdateForm
    template_name = "SubscribersInventory/plandetail_form.html"
    success_url = reverse_lazy("subs_Inv:plan_details")

    def form_valid(self, form):
        messages.success(self.request, " Plan Details updated successfully.")
        return super().form_valid(form)


# SUBSCRIBER STATUS
class SubscribersStatusListView(LoginRequiredMixin, ListView):
    model = SubscriberStatus
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class SubscribersStatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SubscriberStatus
    fields = ["stat_production", "type_of_request", "ready_for_testimony"]
    template_name = "SubscribersInventory/subscriberstatus_form.html"
    success_url = reverse_lazy("subs_Inv:plan_details")

    def form_valid(self, form):
        messages.success(self.request, "Status Updated Successfully.")
        return super().form_valid(form)


# FORWARDING INFORMATION
class ForwardingInfoListView(LoginRequiredMixin, ListView):
    context_object_name = "list"
    queryset = ForwardingInfo.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ForwardingInfoListView, self).get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)

        context["totalnumextension_list"] = TotalNumExtension.objects.all()
        context["totalnumextension_list"] = context["totalnumextension_list"].filter(
            user=self.request.user
        )

        context["ziptrunklogindetail_list"] = ZiptrunkLoginDetail.objects.all()
        context["ziptrunklogindetail_list"] = context[
            "ziptrunklogindetail_list"
        ].filter(user=self.request.user)

        context["otherlogin_list"] = OtherLogin.objects.all()
        context["otherlogin_list"] = context["otherlogin_list"].filter(
            user=self.request.user
        )

        context["notes_list"] = Note.objects.all()
        context["notes_list"] = context["notes_list"].filter(user=self.request.user)

        return context


class ForwardingInfoCreateView(LoginRequiredMixin, CreateView):
    model = ForwardingInfo
    context_object_name = "add"
    form_class = ForwardingInfoCreateForm

    def form_valid(self, form):
        forwardinginfo = form.save(commit=False)
        forwardinginfo.user = self.request.user
        forwardinginfo.save()
        messages.success(self.request, "Forwarding Number Added")
        return redirect("subs_Inv:forward_info")


class ForwardingInfoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ForwardingInfo
    form_class = ForwardingInfoUpdateForm
    template_name = "SubscribersInventory/forwardinginfo_update.html"
    success_url = reverse_lazy("subs_Inv:forward_info")

    def form_valid(self, form):
        messages.success(self.request, "Forwarding Number updated successfully.")
        return super().form_valid(form)


class TotalNumExtensionCreateView(LoginRequiredMixin, CreateView):
    model = TotalNumExtension
    context_object_name = "add"
    form_class = TotalNumExtensionCreateForm

    def form_valid(self, form):
        totalnumextension = form.save(commit=False)
        totalnumextension.user = self.request.user
        totalnumextension.save()
        messages.success(self.request, "Message")
        return redirect("subs_Inv:forward_info")


class TotalNumExtensionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TotalNumExtension
    form_class = TotalNumExtensionUpdateForm
    template_name = "SubscribersInventory/totalnumextension_update.html"
    success_url = reverse_lazy("subs_Inv:forward_info")

    def form_valid(self, form):
        messages.success(self.request, "Number Extension updated successfully.")
        return super().form_valid(form)


class ZiptrunkLoginDetailCreateView(LoginRequiredMixin, CreateView):
    model = ZiptrunkLoginDetail
    context_object_name = "add"
    form_class = ZiptrunkLoginDetailCreateForm

    def form_valid(self, form):
        ziptrunklogindetail = form.save(commit=False)
        ziptrunklogindetail.user = self.request.user
        ziptrunklogindetail.save()
        messages.success(self.request, "Message")
        return redirect("subs_Inv:forward_info")


class ZiptrunkLoginDetailUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = ZiptrunkLoginDetail
    form_class = ZiptrunkLoginDetailUpdateForm
    template_name = "SubscribersInventory/ziptrunklogindetail_update.html"
    success_url = reverse_lazy("subs_Inv:forward_info")

    def form_valid(self, form):
        messages.success(self.request, "Ziptrunk Login updated successfully.")
        return super().form_valid(form)


class OtherLoginCreateView(LoginRequiredMixin, CreateView):
    model = OtherLogin
    context_object_name = "add"
    form_class = OtherLoginCreateForm

    def form_valid(self, form):
        otherlogin = form.save(commit=False)
        otherlogin.user = self.request.user
        otherlogin.save()
        messages.success(self.request, "Other Login updated successfully")
        return redirect("subs_Inv:forward_info")


class OtherLoginUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ZiptrunkLoginDetail
    form_class = OtherLoginUpdateForm
    template_name = "SubscribersInventory/otherlogin_update.html"
    success_url = reverse_lazy("subs_Inv:forward_info")

    def form_valid(self, form):
        messages.success(self.request, "Other Login updated successfully.")
        return super().form_valid(form)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    context_object_name = "add"
    form_class = NoteCreateForm

    def form_valid(self, form):
        notes = form.save(commit=False)
        notes.user = self.request.user
        notes.save()
        messages.success(self.request, "Note added successfilly.")
        return redirect("subs_Inv:forward_info")


class NoteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Note
    form_class = NoteUpdateForm
    template_name = "SubscribersInventory/note_update.html"
    success_url = reverse_lazy("subs_Inv:forward_info")

    def form_valid(self, form):
        messages.success(self.request, "Note updated successfully.")
        return super().form_valid(form)


# class ActivationDetailAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = ForwardingInfo
#     context_object_name = "add"
#     template_name = "SubscribersInventory/activationdetails_addview.html"
#     success_message = "%(activationdetail)s created successfully"

#     def form_valid(self, form):
#         activationdetail = form.save(commit=False)
#         activationdetail.user = self.request.user
#         activationdetail.save()
#         messages.success(self.request, "✔ You have been Created a Details.")
#         return redirect("subs_Inv:activation_details_list")
