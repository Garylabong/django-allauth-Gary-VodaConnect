from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from AccountFiles.forms import ClientFileForm
from AccountFiles.models import *
from django.views.generic import (
    UpdateView,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
)

# Create your views here.
class AccountFilesDetailView(DetailView):
    model = AccountFile
    # context_object_name = "list"
    template_name = "accountfiles/detail.html"


class AccountFilesUpdate(UpdateView):
    form_class = ClientFileForm
    template_name = "AccountFile/personal_file.html"
    success_url = reverse_lazy("auth:client_profile")

    def get_object(self):
        return self.request.user.client

    # def get_queryset(self, *args, **kwargs):
    #     return self.request.accountfile

    # def get_object(self):
    #     return self.request.accountfile


# class ClientProfileUpdate(UpdateView):
#     form_class = ClientEditForm
#     template_name = "authentication/profile_update.html"
#     success_url = reverse_lazy("auth:client_profile")

#     def get_object(self):
#         return self.request.user


# class ClientProfile(DetailView):
#     model = Client
#     template_name = "authentication/profile.html"
#     context_object_name = "list"

#     def get_object(self):
#         return self.request.user
