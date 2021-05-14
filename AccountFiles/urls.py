from django.urls import path

from AccountFiles.views import AccountFilesDetailView

app_name = "acc_file"
urlpatterns = [
    path(
        "accountfiles/<int:pk>",
        AccountFilesDetailView.as_view(),
        name="detail_accfiles",
    )
]
