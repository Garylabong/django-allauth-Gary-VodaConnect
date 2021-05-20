from django.urls import path

from AccountFiles.views import *

app_name = "acc_file"
urlpatterns = [
    path("", AccountFilesList.as_view(), name="account_file"),
    # path(
    #     "order/request/add/",
    #     OrderRequestAddView.as_view(),
    #     name="orderrequest_add",
    # ),
]
