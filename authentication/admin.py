from django.contrib import admin
from authentication.models import Client, User, ClientCode, ClientPersonalFile

admin.site.site_title = "GPG site admin"
admin.site.site_header = "VODACONNECT Administration"
# admin.site.register(Register)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "create_pin",
        "email",
        "is_client",
        "company_name",
        "designation_name",
        "is_active",
    )
    list_filter = ("is_client", "company_name", "designation_name")
    search_fields = ["first_name", "last_name"]


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "first_name",
        "last_name",
        "phone_number",
        "email",
        "affiliate_partner_code",
        "affiliate_partner_name",
        "company_name",
        "designation_name",
        "lead_information",
    )
    list_filter = ("company_name", "designation_name")
    search_fields = ["user", "first_name", "last_name"]

    fieldsets = [
        (
            "Personal information",
            {
                "fields": [
                    "user",
                    "first_name",
                    "last_name",
                    "phone_number",
                    "email",
                ]
            },
        ),
        (
            "User Designation",
            {
                "fields": [
                    "company_name",
                    "designation_name",
                    "affiliate_partner_code",
                    "affiliate_partner_name",
                ]
            },
        ),
        ("Account Authentication", {"fields": ["pin"]}),
        ("Lead Information", {"fields": ["lead_information"]}),
    ]


class ClientPersonalFileline(admin.StackedInline):
    model = ClientPersonalFile
    extra = 1


class ClientCodeAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Client Code", {"fields": ["username", "client_code"]}),
    ]
    inlines = [ClientPersonalFileline]
    list_display = ("username", "client_code")


admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientCode, ClientCodeAdmin)
