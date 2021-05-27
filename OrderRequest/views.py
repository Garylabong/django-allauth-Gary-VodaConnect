from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from OrderRequest.models import *
from OrderRequest.forms import *
from django.views.generic import (
    ListView,
    CreateView,
)


class OrderRequestListView(LoginRequiredMixin, ListView):
    model = OrderRequest
    context_object_name = "list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = context["list"].filter(user=self.request.user)
        return context


class OrderRequestAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = OrderRequest
    form_class = OrderRequestForm
    context_object_name = "add"
    template_name = "OrderRequest/orderrequest_add.html"

    def form_valid(self, form):
        orderrequest = form.save(commit=False)
        orderrequest.user = self.request.user
        orderrequest.save()
        messages.success(self.request, "Request added successfully.")
        return redirect("order_req:order_request")
