# Generated by Django 4.0.1 on 2022-01-12 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bhargav', '0008_rename_iproductid_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='id',
            new_name='iProductId',
        ),
    ]
