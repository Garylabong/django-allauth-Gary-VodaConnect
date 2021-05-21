from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    path("profile/", ClientProfile.as_view(), name="client_profile"),
    path("profile/update", ClientProfileUpdate.as_view(), name="update_profile"),
    path(
        "profile/update/information",
        ClientInformationUpdate.as_view(),
        name="update_information",
    ),
    # PERSONAL FILES
    path("personalfile/", PersonalFilesListView.as_view(), name="personal_file_list"),
    path(
        "personalfile_create/",
        PersonalFilesCreateView.as_view(),
        name="personalfile_create",
    ),
    path(
        "personal_file/<int:pk>/",
        PersonalFilesUpdateView.as_view(),
        name="personal_file_update",
    ),
]
