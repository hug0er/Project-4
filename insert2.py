import pandas as pd
from features.models import TimeSeriesValues

names = ["Series 1","Series 2","Series 3","Series 4","Series 5","Series 6","Series 7", "Series 8", "Series 9","Series 10","Series 11","Series 12"]

Series = pd.read_excel("NN3_FINAL_DATASET_WITH_TEST_DATA.xlsx", sheet_name="Hoja 1")

lst = []
for i in Series:
    lst.append(i)

lst.pop(12)

names = zip(names,lst)

for a in names:
    series = TimeSeriesValues()
    series.Name = a[0]
    series.values = Series[a[1]].dropna().values
    series.save()  


