# Generated by Django 5.1 on 2024-09-02 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTomas', '0003_cart_client_rename_products_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
