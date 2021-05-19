from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    # path("profile/<slug>/", ClientProfileAddView.as_view(), name="profile"),
    # path("profile/<int:pk>/", ClientProfileDetailView.as_view(), name="profile_detail"),
    path("profile/", ClientProfile.as_view(), name="client_profile"),
    path("profile/update", ClientProfileUpdate.as_view(), name="update_profile"),
    path(
        "profile/update/information",
        ClientInformationUpdate.as_view(),
        name="update_information",
    ),
    # path(
    #     "profile/update/information",
    #     ClientPersonalFileDetail.as_view(),
    #     name="update_",
    # ),
]
