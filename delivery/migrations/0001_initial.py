# Generated by Django 5.1.2 on 2024-10-25 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.BigIntegerField()),
                ('courier', models.BigIntegerField()),
                ('delivery_time', models.BigIntegerField()),
                ('delivered_at', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Deliveries',
                'db_table': 'delivery',
                'ordering': ['-delivered_at'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='delivery.delivery')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'db_table': 'review',
                'ordering': ['-created_at'],
            },
        ),
    ]
