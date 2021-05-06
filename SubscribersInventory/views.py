from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views import View
from .views import *


@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "VOIPLine/home.html"


class SubsInvView(View):
    def get(self, request):
        return render(request, "VOIPLine/subs_inventory.html")

class VoipInfoView(View):
    def get(self, request):
        return render(request, "VOIPLine/Voip_info.html")

class ActivationDetailsView(View):
    def get(self, request):
        return render(request, "VOIPLine/activation_details.html")

class PlanDetailsView(View):
    def get(self, request):
        return render(request, "VOIPLine/plan_details.html")

class SubscribersStatusView(View):
    def get(self, request):
        return render(request, "VOIPLine/subs_status.html")

class ForwardingInfoView(View):
    def get(self, request):
        return render(request, "VOIPLine/forwarding_info.html")
