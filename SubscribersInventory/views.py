from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ActivationDetailForm
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
)
from django.views import View
from .views import *
from .models import *


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "SubscribersInventory/home.html"


class SubsInvView(TemplateView):
    template_name = "SubscribersInventory/subs_inventory.html"


class VoipListView(ListView):
    model = VoIpInformation

    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.vodaconnect_number)
        return context


class VoipDetailView(DetailView):
    model = VoIpInformation
    context_object_name = "detail"
    template_name = "SubscribersInventory/voipinformation_detail.html"


class ActivationDetailListView(ListView):
    model = ActivationDetail
    context_object_name = "list"
    template_name = "SubscribersInventory/activationdetail_list.html"


class ActivationDetailView(DetailView):
    model = ActivationDetail
    # context_object_name = "details"
    template_name = "SubscribersInventory/activation_detail.html"
    # queryset = ActivationDetail.objects.all()

    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(ActivationDetail, id=id_)


# class AccountFilesDetailView(DetailView):
#     model = AccountFile
#     # context_object_name = "list"
#     template_name = "accountfiles/detail.html"


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
        messages.success(self.request, "You have been Created a Details!")
        return redirect("subs_Inv:activation_details_list")


class PlanDetailsView(TemplateView):
    template_name = "SubscribersInventory/plan_details.html"


class PlanDetailsListView(ListView):
    model = PlanDetail
    context_object_name = "list"
    # template_name = "SubscribersInventory/activationdetail_list.html"


class SubscribersStatusView(TemplateView):
    template_name = "SubscribersInventory/subs_status.html"


class ForwardingInfoView(TemplateView):
    template_name = "SubscribersInventory/forwarding_info.html"


class ProfileView(TemplateView):
    template_name = "SubscribersInventory/profile.html"


class OtherChargeView(TemplateView):
    template_name = "SubscribersInventory/other_charge.html"


class MonthlyChargeView(TemplateView):
    template_name = "SubscribersInventory/monthly_charge.html"


class OrderRequestView(TemplateView):
    template_name = "SubscribersInventory/order_request.html"
