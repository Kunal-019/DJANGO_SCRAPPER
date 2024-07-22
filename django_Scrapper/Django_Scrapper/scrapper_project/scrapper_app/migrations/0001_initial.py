# Generated by Django 5.0.6 on 2024-06-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('country_code', models.IntegerField()),
                ('ISO_CODE', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('gdp', models.FloatField()),
            ],
        ),
    ]