from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
