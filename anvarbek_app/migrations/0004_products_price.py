# Generated by Django 4.0.1 on 2022-01-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anvarbek_app', '0003_alter_products_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10000000, max_digits=1000, verbose_name='Цена'),
        ),
    ]
