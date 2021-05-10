from django.urls import path
from OrderRequest.views import *

app_name = "order_req"
urlpatterns = [
    path("order/request/", OrderRequestListView.as_view(), name="order_request"),
]
