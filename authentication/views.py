from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
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
from AccountFiles.models import *
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


class ClientProfileUpdate(LoginRequiredMixin, UpdateView):
    form_class = ClientEditForm
    template_name = "authentication/profile_update.html"
    success_url = reverse_lazy("auth:client_profile")

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Client Profile updated successfully!")
        return super().form_valid(form)


class ClientInformationUpdate(LoginRequiredMixin, UpdateView):
    form_class = ClientEditInfoForm
    template_name = "authentication/update_information.html"
    success_url = reverse_lazy("auth:client_profile")

    def get_object(self):
        return self.request.user.client

    def form_valid(self, form):
        messages.success(self.request, "Client Information updated successfully!")
        return super().form_valid(form)


class ClientProfile(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "authentication/profile.html"
    context_object_name = "list"

    def get_object(self):
        return self.request.user


class ClientPersonalFileDetail(LoginRequiredMixin, DetailView):
    model = ClientPersonalFile
    context_object_name = "list"


class PersonalFilesListView(LoginRequiredMixin, ListView):
    model = ClientPersonalFile
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class PersonalFilesCreateView(LoginRequiredMixin, CreateView):
    model = ClientPersonalFile
    fields = [
        "client",
        "file_title",
        "url",
        "description",
    ]
    template_name = "authentication/clientpersonalfile_create.html"
    success_url = reverse_lazy("auth:personal_file_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PersonalFilesCreateView, self).form_valid(form)


class PersonalFilesUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientPersonalFile
    fields = ["client", "file_title", "url", "description"]
    template_name = "authentication/clientpersonalfile_form.html"
    success_url = reverse_lazy("auth:personal_file_list")
