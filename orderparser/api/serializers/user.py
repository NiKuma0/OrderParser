from rest_framework import serializers as schema

from orderparser.api.models import Customer


class CustomerSerializer(schema.ModelSerializer[Customer]):
    spent_money = schema.IntegerField(help_text="Total spent amount")
    gems = schema.ListField(
        child=schema.CharField(max_length=256, label="gem", help_text="Gemstone name"),
        help_text="Popular gemstones purchased by this customer.",
    )

    class Meta:
        model = Customer
        fields = ("username", "spent_money", "gems")
