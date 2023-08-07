from django.db import models


class Customer(models.Model):
    username = models.SlugField("Customer username (slug)", max_length=256, primary_key=True)

    def __str__(self) -> str:
        return f"Customer: {self.username}"


class Item(models.Model):
    name = models.CharField("Item name", max_length=256, primary_key=True)

    def __str__(self) -> str:
        return f"Item: {self.name}"


class Deal(models.Model):
    customer = models.ForeignKey(
        Customer,
        to_field="username",
        on_delete=models.CASCADE,
        related_name="deals",
    )
    item = models.ForeignKey(
        Item,
        to_field="name",
        on_delete=models.CASCADE,
        related_name="deals",
    )
    total = models.IntegerField("Total amount")
    quantity = models.IntegerField("Quantity items")
    date = models.DateTimeField("Registered Date")

    def __str__(self) -> str:
        return f"Order: {self.customer.username} buys a {self.item.name}. ({self.pk})"
