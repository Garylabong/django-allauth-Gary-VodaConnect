from django.urls import path
from Billing.views import *

app_name = "bill"
urlpatterns = [
    # MONTHLY CHARGE
    path("", MonthlyChargeList.as_view(), name="month_list"),
    path("monthlycharge/<int:pk>/", MonthlyChargeDetail.as_view(), name="month_detail"),
    path(
        "monthlycharge_create/",
        MonthlyChargeCreate.as_view(),
        name="month_create",
    ),
    path(
        "monthlycharge_update/<int:pk>/",
        MonthlyChargeUpdate.as_view(),
        name="month_Update",
    ),
    path(
        "monthlycharge_delete/<int:pk>/",
        MonthlyChargeDelete.as_view(),
        name="month_delete",
    ),
    # OTHER CHARGE
    path("othercharge/", OtherChargeListView.as_view(), name="othercharge_list"),
    path(
        "othercharge_create/",
        OtherChargeCreateView.as_view(),
        name="othercharge_create",
    ),
    path(
        "othercharge_update/<int:pk>/",
        OtherChargeUpdateView.as_view(),
        name="othercharge_update",
    ),
]
