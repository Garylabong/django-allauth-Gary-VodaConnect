from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from authentication.forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    UpdateView,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
)

# from django.conf.auth.decorators import login_required

from .models import Client
from .serializers import ClientSerializer

from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated


@login_required
def dashboard(request):
    return render(request, "")


class ClientViewSet(viewsets.ModelViewSet):
    authentication_classes = (BaseAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


from django.http import JsonResponse
from authentication.models import Client


def index(request):
    authentications = []

    for authentication in Client.objects.all():
        authentications.append(
            {
                "username": authentication.username,
                "firstname": authentication.first_name,
            }
        )

    return JsonResponse(authentications, safe=False)


class ClientProfileUpdate(UpdateView):
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "affiliate_partner_code",
        "affiliate_partner_name",
        "pin",
        "company_name",
        "designation_name",
        "lead_information",
    ]
    template_name = "authentication/profile_update.html"
    success_url = reverse_lazy("client_profile")

    def get_object(self):
        return self.request.user.is_client


class ClientProfile(DetailView):
    model = Client
    template_name = "authentication/profile.html"
    context_object_name = "list"
    # success_url = reverse_lazy("client_profile")

    def get_object(self):
        return self.request.user.is_client


class ClientProfileDetailView(DetailView):
    model = Client
    # form_class = ClientAddForm
    context_object_name = "add"
    # success_url = "/profile/"
    template_name = "authentication/clientprofile_form.html"


class ClientProfileAddView(CreateView):
    model = Client
    form_class = ClientAddForm
    context_object_name = "add"
    template_name = "authentication/clientprofile_form.html"

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user.client
        client.save()
        messages.success(self.request, "You have been Created a Details!")
        return redirect("subs_Inv:activation_details_list")
