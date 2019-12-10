# Generated by Django 3.0 on 2019-12-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chaos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Periodicity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('SelfSimilarity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Variance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Energy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Kurtosis', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Partial_autocorrelation_12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Partial_autocorrelation_2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Partial_autocorrelation_1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Autocorrelation_12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Autocorrelation_2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Autocorrelation_1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Sweekness', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Trend', models.DecimalField(decimal_places=2, max_digits=5)),
                ('LSTM', models.DecimalField(decimal_places=2, max_digits=5)),
                ('FFNN', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
