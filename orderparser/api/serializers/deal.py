from typing import Any

from rest_framework import serializers as schema

from orderparser.api.models import Customer, Deal, Item


class DealSerializer(schema.ModelSerializer[Deal]):
    customer = schema.SlugField(max_length=256)
    item = schema.CharField(max_length=256)

    class Meta:
        model = Deal
        fields = "__all__"

    def create(self, validated_data: dict[str, Any]) -> Deal:
        if validated_data:
            validated_data["item"], _ = Item.objects.get_or_create(name=validated_data["item"])
            validated_data["customer"], _ = Customer.objects.get_or_create(username=validated_data["customer"])
        return super().create(validated_data)


class DealCreateSerializer(schema.Serializer[Any]):
    deals = schema.FileField(required=True)

    def create(self, validated_data: Any) -> Any:
        ...

    def update(self, instance: Any, validated_data: Any) -> Any:
        ...
