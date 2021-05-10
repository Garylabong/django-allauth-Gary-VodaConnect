from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    context_object_name = "voip"
    paginate_by = 4


class VoipDetailView(DetailView):
    model = VoIpInformation
    context_object_name = "voip"
    template_name = "SubscribersInventory/voipinformation_detail.html"


class ActivationDetailsView(TemplateView):
    template_name = "SubscribersInventory/activation_details.html"


class ActivationDetailAddView(CreateView):
    model = ActivationDetail
    fields = (
        "order_request_date",
        "request_date_initiated",
        "date_line_activated",
        "date_line_terminated",
        "phone_line_status",
        "client_company_user",
    )
    context_object_name = "add"
    template_name = "SubscribersInventory/activationdetails_addview.html"


class PlanDetailsView(TemplateView):
    template_name = "SubscribersInventory/plan_details.html"


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
