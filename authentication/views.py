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
from authentication.models import *
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
    form_class = ClientEditForm
    template_name = "authentication/profile_update.html"
    success_url = reverse_lazy("auth:client_profile")

    def get_object(self):
        return self.request.user


class ClientInformationUpdate(UpdateView):
    form_class = ClientEditInfoForm
    template_name = "authentication/update_information.html"
    success_url = reverse_lazy("auth:client_profile")

    def get_object(self):
        return self.request.user.client


class ClientProfile(DetailView):
    model = Client
    template_name = "authentication/profile.html"
    context_object_name = "list"

    def get_object(self):
        return self.request.user


class ClientPersonalFileDetail(DetailView):
    model = ClientPersonalFile
    template_name = ""
    context_object_name = "list"
