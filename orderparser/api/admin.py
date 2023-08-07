from django.contrib import admin

from .models import Customer, Deal, Item


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    ...


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    ...
