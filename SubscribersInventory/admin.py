from django.contrib import admin
from SubscribersInventory.models import (
    VOIPInformation,
    ActivationDetail,
    PlanDetail,
    SubscriberStatus,
    ForwardingInfo,
    TotalNumExtension,
    ZiptrunkLoginDetail,
    OtherLogin,
    Note,
    PlanType,
    VodaConnectNumber,
)

# Register your models here.

admin.site.register(VodaConnectNumber)
admin.site.register(VOIPInformation)
admin.site.register(ActivationDetail)
admin.site.register(PlanDetail)
admin.site.register(SubscriberStatus)
admin.site.register(ForwardingInfo)
admin.site.register(TotalNumExtension)
admin.site.register(ZiptrunkLoginDetail)
admin.site.register(OtherLogin)
admin.site.register(Note)
admin.site.register(PlanType)
