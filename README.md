# Project 4


The structure of the following project goes as follows: 

Folder timeSeries:
- timeSeries folder contains some predetermined files.
- **NN3_FINAL_DATASET_WITH_TEST_DATA ** contains the data to fill up TimeSeriesValues .
- **data.txt ** contains the data to fill up TimeSeriesValues .
- **insert.py ** file is used to insert automatically all of the elemens from data.txt.
- **insert2.py ** file is used to insert automatically all of the elemens from NN3_FINAL_DATASET_WITH_TEST_DATA.

Folder features:
- Static folder contains both css and js files.
- Templates folder contains all the html files used in this project:
1. **base.html:** contains a navigation bar which is extended to almost every other html file. Also, have the all the imports of boostrap.
2. **features.html:** It contains a form that allows us to select the characteristics that we want to obtain from the time series.
3. **featuresSerie.html:** It contains two javascript Canvas that allow us to graph the time series, in addition to a button that graphs the series without trend.


All other files use the django standard. For example, view.py has all the functions, urls all the paths and models.py the database models.


**Note :** is important install numpy, pandas and sklearn used to **detrend** the time series. Using bootstrap, we take care of making smaller devices use a scrollbar to navigate the features.


