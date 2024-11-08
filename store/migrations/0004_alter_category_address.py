# Generated by Django 5.1 on 2024-11-08 04:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
        ("store", "0003_alter_category_options_alter_subcategory_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="common.address",
                verbose_name="Manzil",
            ),
        ),
    ]
