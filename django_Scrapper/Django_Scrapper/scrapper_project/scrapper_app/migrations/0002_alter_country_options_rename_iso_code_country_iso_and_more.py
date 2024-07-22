# Generated by Django 4.2.13 on 2024-06-11 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'countries_data'},
        ),
        migrations.RenameField(
            model_name='country',
            old_name='ISO_CODE',
            new_name='iso',
        ),
        migrations.AddField(
            model_name='country',
            name='area',
            field=models.IntegerField(default=0),
        ),
    ]
