# Generated by Django 4.1.2 on 2022-10-20 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='brand',
        ),
    ]
