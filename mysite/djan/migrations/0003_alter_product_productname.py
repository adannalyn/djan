# Generated by Django 4.0.5 on 2022-06-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djan', '0002_remove_product_promo_remove_product_sales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productname',
            field=models.CharField(default='', max_length=200),
        ),
    ]