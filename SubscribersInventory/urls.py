from django.urls import path
from .views import VoipListView
from SubscribersInventory.views import *

app_name = "subs_Inv"
urlpatterns = [
    path("", home, name="home"),
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
    path(
        "forwardinginformation/add/",
        ForwardingInfoCreateView.as_view(),
        name="forwardinginformation_add",
    ),
    path(
        "totalnumextension/add/",
        TotalNumExtensionCreateView.as_view(),
        name="totalnumextension_add",
    ),
    path(
        "ziptrunklogindetail/add/",
        ZiptrunkLoginDetailCreateView.as_view(),
        name="ziptrunklogindetail_add",
    ),
    path(
        "otherlogin/add/",
        OtherLoginCreateView.as_view(),
        name="otherlogin_add",
    ),
    path(
        "notes/add/",
        NoteCreateView.as_view(),
        name="notes_add",
    ),
    path(
        "forwardinfo/update/<int:pk>/",
        ForwardingInfoUpdateView.as_view(),
        name="forwardinfo_update",
    ),
    path(
        "totalnum/extension/update/<int:pk>/",
        TotalNumExtensionUpdateView.as_view(),
        name="totalnumextension_update",
    ),
    path(
        "ziptrunk/update/<int:pk>/",
        ZiptrunkLoginDetailUpdateView.as_view(),
        name="ziptrunklogindetail_update",
    ),
    path(
        "otherlogin/update/<int:pk>/",
        OtherLoginUpdateView.as_view(),
        name="otherlogin_update",
    ),
    path(
        "notes/update/<int:pk>/",
        NoteUpdateView.as_view(),
        name="notes_update",
    ),
]
