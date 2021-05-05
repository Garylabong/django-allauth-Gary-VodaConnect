from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views import View
from .views import *


@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        return render(request, "VOIPLine/home.html")
