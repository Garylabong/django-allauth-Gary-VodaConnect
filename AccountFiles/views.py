from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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


class AccountFilesList(LoginRequiredMixin, ListView):
    model = AccountFile
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class AccountFilesCreate(LoginRequiredMixin, CreateView):
    model = AccountFile
    form_class = ClientFileForm
    template_name = "AccountFiles/accountfile_add.html"
    success_url = reverse_lazy("acc_file:account_file")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccountFilesCreate, self).form_valid(form)

    def form_valid(self, form):
        messages.success(self.request, "Client File created successfully!")
        return super().form_valid(form)
