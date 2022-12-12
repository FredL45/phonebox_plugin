from rest_framework import serializers
from phonebox_plugin import models
# for netbox 3.3
try:
from netbox.api import WritableNestedSerializer
except ImportError:
from netbox.api.serializers.nested import WritableNestedSerializer

from tenancy.api.nested_serializers import NestedTenantSerializer

__all__ = ["NestedNumberSerializer", ]


class NestedNumberSerializer(WritableNestedSerializer):

    label = serializers.CharField(source='number', read_only=True)
    tenant = NestedTenantSerializer(required=True, allow_null=False)

    class Meta:
        model = models.Number
        fields = [
            "id", "label", "number", "tenant",
        ]
