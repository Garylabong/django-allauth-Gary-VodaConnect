from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    # path("profile/<slug>/", ClientProfileAddView.as_view(), name="profile"),
    path("profile/<int:pk>/", ClientProfileDetailView.as_view(), name="profile_detail"),
    path(
        "profile/<int:pk>/edit",
        ClientProfileEditView.as_view(),
        name="edit_profile",
    ),
]
