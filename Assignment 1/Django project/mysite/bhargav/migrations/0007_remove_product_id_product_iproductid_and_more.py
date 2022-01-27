# Generated by Django 4.0.1 on 2022-01-12 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhargav', '0006_product_pdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AddField(
            model_name='product',
            name='iProductId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='pDate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date (mm/dd/yy)'),
        ),
    ]