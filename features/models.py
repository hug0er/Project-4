from django.db import models

# Create your models here.
class TimeSeries(models.Model):

    Name = models.CharField(
        max_length=64,
        null=True
    )
    Chaos = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Periodicity = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    SelfSimilarity = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Nonlinearity = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Variance = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Energy = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Kurtosis = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Partial_autocorrelation_12 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Partial_autocorrelation_2 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Partial_autocorrelation_1 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Autocorrelation_12 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Autocorrelation_2 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Autocorrelation_1 = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Sweekness = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    Trend = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    LSTM = models.DecimalField( null=True, max_digits=13, decimal_places=10)
    FFNN  = models.DecimalField( null=True, max_digits=13, decimal_places=10)

class TimeSeriesValues(models.Model):
    Name = models.CharField(
        max_length=64,
        null=True
    )
    values = models.CharField(null=True, max_length=2000) 
