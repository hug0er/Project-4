# Generated by Django 3.0 on 2019-12-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_timeseriesvalues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeseriesvalues',
            name='values',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]