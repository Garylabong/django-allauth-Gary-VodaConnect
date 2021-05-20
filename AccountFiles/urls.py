from django.urls import path

from AccountFiles.views import *

app_name = "acc_file"
urlpatterns = [
    path("", AccountFilesList.as_view(), name="account_file"),
    path(
        "accountfile/add/",
        AccountFilesCreate.as_view(),
        name="accountfile_add",
    ),
]
