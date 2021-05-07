from django.urls import path
from .views import VoipListView
from SubscribersInventory.views import *

app_name = "subs_Inv"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("subscribers/inventory/", SubsInvView.as_view(), name="subs_inv"),
    # path("voip/information/", VoipInfoView.as_view(), name="voip_info"),
    path(
        "activation/details/",
        ActivationDetailsView.as_view(),
        name="activation_details",
    ),
    path("plan/details/", PlanDetailsView.as_view(), name="plan_details"),
    path("subscribers/status/", SubscribersStatusView.as_view(), name="subs_status"),
    path("forwarding/information/", ForwardingInfoView.as_view(), name="forward_info"),
    path("profile/", ProfileView.as_view(), name="profile"),
    # CRUD
    path("voip/information/", VoipListView.as_view(), name="voip_info"),
]
