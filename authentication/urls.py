from django.urls import path

from authentication.views import *

app_name = "auth"
urlpatterns = [
    path("authentication/", index),
    path("<int:pk>/", ClientProfileUpdate.as_view(), name="edit_profile"),
]
