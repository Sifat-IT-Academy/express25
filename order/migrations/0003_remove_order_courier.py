# Generated by Django 5.1.2 on 2024-12-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_productorder_options_alter_order_courier_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='courier',
        ),
    ]
