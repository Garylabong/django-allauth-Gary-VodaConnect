from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
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


class ActivationDetailsView(TemplateView):
    template_name = "SubscribersInventory/activation_details.html"


class PlanDetailsView(TemplateView):
    template_name = "SubscribersInventory/plan_details.html"


class SubscribersStatusView(TemplateView):
    template_name = "SubscribersInventory/subs_status.html"


class ForwardingInfoView(TemplateView):
    template_name = "SubscribersInventory/forwarding_info.html"


class ProfileView(TemplateView):
    template_name = "SubscribersInventory/profile.html"
