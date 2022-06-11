# Generated by Django 4.0.5 on 2022-06-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='promo',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sales',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='product',
            name='productname',
            field=models.CharField(default='Quality', max_length=200),
        ),
    ]
