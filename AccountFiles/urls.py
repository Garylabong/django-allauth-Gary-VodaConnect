from django.urls import path

from AccountFiles.views import AccountFilesDetailView, AccountFilesUpdate

app_name = "acc_file"
urlpatterns = [
    path(
        "accountfiles/<int:pk>",
        AccountFilesDetailView.as_view(),
        name="detail_accfiles",
    ),
    path(
        "profile/personal/file",
        AccountFilesUpdate.as_view(),
        name="personal_file",
    ),
]
