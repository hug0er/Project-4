import csv
from features.models import TimeSeries

f = open('data.txt', 'r')  

for line in f:  
    line =  line.split(',')  
    series = TimeSeries() 
    series.Name = line[0]
    series.Chaos = round(float(line[17] ), 5)
    series.Periodicity = round(float(line[16] ), 5)
    series.SelfSimilarity = round(float(line[15] ), 5)
    series.Nonlinearity = round(float(line[14] ), 5)
    series.Variance = round(float(line[13] ), 5)
    series.Energy = round(float(line[12] ), 5)
    series.Kurtosis = round(float(line[11] ), 5)
    series.Partial_autocorrelation_12 = round(float(line[10] ), 5)
    series.Partial_autocorrelation_2 = round(float(line[9] ), 5)
    series.Partial_autocorrelation_1 = round(float(line[8] ), 5)
    series.Autocorrelation_12 = round(float(line[7] ), 5)
    series.Autocorrelation_2 = round(float(line[6] ), 5)
    series.Autocorrelation_1 = round(float(line[5] ), 5)
    series.Sweekness = round(float(line[4] ), 5)
    series.Trend = round(float(line[3] ), 5)
    series.LSTM = round(float(line[1] ), 5)
    series.FFNN = round(float(line[2] ), 5)
    series.save()  

f.close()

