# Generated by Django 3.0.7 on 2020-06-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('variantsViz', '0006_auto_20200630_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='reaal_path_file',
        ),
        migrations.AddField(
            model_name='table',
            name='real_path_file',
            field=models.FilePathField(default='def', path='/home/maelle/Bureau/Stage/'),
            preserve_default=False,
        ),
    ]
