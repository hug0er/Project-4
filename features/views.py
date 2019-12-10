from django.shortcuts import render
from . import models
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd

def trend_imp(Serie_flat):
    Serie_flat = np.array(Serie_flat)
    x = list(range(0,len(Serie_flat)))
    x = np.array(x)
    x = x/len(x)
    x = x[:, np.newaxis]
    Serie_flat2 = Serie_flat[:, np.newaxis]
    polynomial_features= PolynomialFeatures(degree=3)
    x_poly = polynomial_features.fit_transform(x)
    model = LinearRegression()
    model.fit(x_poly, Serie_flat2)
    y_poly_pred = model.predict(x_poly)
    return (Serie_flat2-y_poly_pred)


# Create your views here.
def home(request):
    return render(request, "home.html")

def features(request):

    if request.method == 'GET':
        return render(request, "features.html")

def featuresSerie(request):

    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        series = data.get('series')
        features = data.getlist('features')
        model = models.TimeSeries.objects.filter(Name=series)
        model = model[0]
        lst = []
        for i in features:
            lst.append(getattr( model, i ) )
        points = models.TimeSeriesValues.objects.filter(Name=series)
        points = points[0].values
        points = points.translate({ord(i): None for i in '[]\n'}) 
        points = points.split(" ")  
        p = []
        for i in points:
            try: 
                p.append(float(i))
            except:
                pass
        p2 = trend_imp(p)
        pointsy = []
        pointsy2 = []
        for i in p:
            pointsy.append({'y' : i})
        for i in p2:
            pointsy2.append({'y' : round(i[0],2)})
        
        context = {
            "name" : name,
            "series" : series,
            "features" : features,
            "values" : lst,
            "pointsy" : pointsy,
            "pointsy2" : pointsy2
        }
        print(pointsy2)
        return render(request, "featuresSerie.html", context)
