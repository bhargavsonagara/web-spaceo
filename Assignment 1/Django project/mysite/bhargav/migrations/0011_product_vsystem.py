# Generated by Django 4.0.1 on 2022-01-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhargav', '0010_product_pdatetime_alter_product_pdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vSystem',
            field=models.CharField(choices=[('a', 'Automatic'), ('m', 'Manual')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]