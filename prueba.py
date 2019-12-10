#names = "Series 1","Series 2","Series 3","Series 4","Series 5","Series 6","Series 7", "Series 9","Series 10","Series 11","Series 12"
names = ["Chaos","Periodicity","Self-Similarity","Variance","Energy","Kurtosis","Partial_autocorrelation_12","Partial_autocorrelation_2","Partial_autocorrelation_1","Autocorrelation_12","Autocorrelation_2","Autocorrelation_1","Sweekness","Trend","LSTM","FFNN "]

for i in names:

    print ( i  + " = models.DecimalField( null=True, max_digits=5, decimal_places=2)")