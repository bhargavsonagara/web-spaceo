# Generated by Django 4.0.1 on 2022-01-12 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhargav', '0002_product_vtitle1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dates',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date(mm/dd/2022)'),
        ),
    ]
