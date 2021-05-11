from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    # path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/", ClientProfileAddView.as_view(), name="profile"),
    path(
        "profile/<int:pk>/edit/",
        ClientProfileUpdate.as_view(),
        name="edit_profile",
    ),
    # path("order/request/", OrderRequestListView.as_view(), name="order_request"),
]
