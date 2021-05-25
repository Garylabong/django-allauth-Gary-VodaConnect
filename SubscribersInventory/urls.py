from django.urls import path
from .views import VoipListView
from SubscribersInventory.views import *

app_name = "subs_Inv"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("subscribers/inventory/", SubsInvView.as_view(), name="subs_inv"),
    # vOIPiNFO
    path("voip/information/", VoipListView.as_view(), name="voip_info"),
    # ACTIVATION DETAILS
    path(
        "activation/details/",
        ActivationDetailListView.as_view(),
        name="activation_details_list",
    ),
    path(
        "activation/details/add/",
        ActivationDetailAddView.as_view(),
        name="activation_details_add",
    ),
    # PLAN DETAILS
    path("plan/details/", PlanDetailsListView.as_view(), name="plan_details"),
    path(
        "plan/details/<int:pk>/",
        PlanDetailsUpdateView.as_view(),
        name="plan_details_update",
    ),
    # SUBSCRIBER sTATUS
    path(
        "subscribers/status/", SubscribersStatusListView.as_view(), name="subs_status"
    ),
    path(
        "subscribers/status/<int:pk>/",
        SubscribersStatusUpdateView.as_view(),
        name="subs_status_update",
    ),
    # FORWARDING INFORMATION
    path(
        "forwardinginformation/", ForwardingInfoListView.as_view(), name="forward_info"
    ),
]
