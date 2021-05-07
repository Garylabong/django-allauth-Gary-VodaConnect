from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views import View
from .views import *


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "VOIPLine/home.html"


class SubsInvView(TemplateView):
    template_name = "VOIPLine/subs_inventory.html"

class VoipInfoView(TemplateView):
    template_name = "VOIPLine/Voip_info.html"

class ActivationDetailsView(TemplateView):
    template_name = "VOIPLine/activation_details.html"


class PlanDetailsView(TemplateView):
    template_name = "VOIPLine/plan_details.html"

class SubscribersStatusView(TemplateView):
    template_name = "VOIPLine/subs_status.html"


class ForwardingInfoView(TemplateView):
    template_name = "VOIPLine/forwarding_info.html"
   

class ProfileView(TemplateView):
    template_name = "VOIPLine/profile.html"

