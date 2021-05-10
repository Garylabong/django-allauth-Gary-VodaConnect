from django.urls import path
from .views import VoipListView
from SubscribersInventory.views import *

app_name = "subs_Inv"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("subscribers/inventory/", SubsInvView.as_view(), name="subs_inv"),
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
    path("plan/details/", PlanDetailsView.as_view(), name="plan_details"),
    path("subscribers/status/", SubscribersStatusView.as_view(), name="subs_status"),
    path("forwarding/information/", ForwardingInfoView.as_view(), name="forward_info"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("other/charge", OtherChargeView.as_view(), name="other_charge"),
    path("monthly/charge", MonthlyChargeView.as_view(), name="monthly_charge"),
    path("order/request", OrderRequestView.as_view(), name="order_request"),
    # CRUD
    path("voip/information/", VoipListView.as_view(), name="voip_info"),
    path("voip/information/<int:pk>", VoipDetailView.as_view(), name="voip_info"),
]
