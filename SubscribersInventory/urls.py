from django.urls import path

from SubscribersInventory.views import HomeView


urlpatterns = [path("", HomeView.as_view(), name="home")]
