from django.db import models
from django.db.models.query import QuerySet

from orderparser.api.models import Customer, Item
from orderparser.api.serializers import CustomerSerializer

from .base import ListViewSet


class UserViewSet(ListViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):  # type: ignore
        queryset: QuerySet[Customer] = super().get_queryset()
        customers = (
            queryset.annotate(
                spent_money=models.Sum(
                    "deals__total",
                )
            )
            .order_by("-spent_money")[:5]
            .values()
        )

        for customer in customers:
            customer["gems"] = (
                Item.objects.filter(deals__customer_id__in=customers.values("username"))
                .filter(deals__customer_id=customer["username"])
                .annotate(models.Count("name"))
                .order_by("name")
                .values_list("name", flat=True)
            )
        return customers
