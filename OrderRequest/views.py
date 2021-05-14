from django.contrib import messages
from django.shortcuts import render, redirect
from OrderRequest.models import *
from OrderRequest.forms import *
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    FormView,
)


class OrderRequestListView(ListView):
    model = OrderRequest
    context_object_name = "OrderRequest"


class OrderRequestAddView(CreateView):
    model = OrderRequest
    form_class = OrderRequestForm
    # fields = (
    #     "date_request",
    #     "plan_type",
    #     "company_name",
    #     "address",
    #     "preferred_code",
    #     "phone_number",
    #     "fax",s
    #     "request",
    #     "category_request",
    #     "email",
    #     "order_status",
    #     "notes",
    # )
    context_object_name = "add"
    template_name = "OrderRequest/orderrequest_add.html"

    def form_valid(self, form):
        orderrequest = form.save(commit=False)
        orderrequest.user = self.request.user
        orderrequest.save()
        messages.success(self.request, "You have been Created a Details!")
        return redirect("order_req:order_request")
