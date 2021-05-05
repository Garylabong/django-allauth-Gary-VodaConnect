from django.shortcuts import render, redirect
from django.views.generic import View
from django.views import View
from .views import *


class HomeView(View):
    def get(self, request):
        return render(request, "VOIPLine/home.html")
