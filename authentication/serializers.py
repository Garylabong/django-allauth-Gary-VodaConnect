from rest_framework import serializers

from .models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "company_category",
            "designation_category",
            "affiliate_partner_code",
            "affiliate_partner_name",
            "pin",
            "lead_information",
        )
