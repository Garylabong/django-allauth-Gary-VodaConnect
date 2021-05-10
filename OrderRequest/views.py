from django.shortcuts import render
from OrderRequest.models import *
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
