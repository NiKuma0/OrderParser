# Generated by Django 4.2.4 on 2023-08-07 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_customer_alter_deal_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deal",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="deals", to="api.customer"
            ),
        ),
    ]
