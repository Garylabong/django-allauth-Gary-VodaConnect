from django.urls import path
from .views import VoipListView
from SubscribersInventory.views import *

app_name = "subs_Inv"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("subscribers/inventory/", SubsInvView.as_view(), name="subs_inv"),
    path("subscribers/status/", SubscribersStatusView.as_view(), name="subs_status"),
    path("forwarding/information/", ForwardingInfoView.as_view(), name="forward_info"),
    path("other/charge", OtherChargeView.as_view(), name="other_charge"),
    path("monthly/charge", MonthlyChargeView.as_view(), name="monthly_charge"),
    # CRUD
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
]
