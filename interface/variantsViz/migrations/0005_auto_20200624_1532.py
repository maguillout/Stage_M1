# Generated by Django 3.0.7 on 2020-06-24 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('variantsViz', '0004_all_products_timeseries'),
    ]

    operations = [
        migrations.DeleteModel(
            name='all_products',
        ),
        migrations.DeleteModel(
            name='TimeSeries',
        ),
    ]
