#############################################
# This program will plot and spit out the 
# accuracy of the forecast given the provided
# data and number of days out.
# sys.argv[1] is days out (0-7)
# sys.argv[2] is forecast file
# sys.argv[3] is actuals file
#############################################

import sys
import datetime
import matplotlib.pyplot as plt

daysOut = int(sys.argv[1])
assert(daysOut > -1 and daysOut < 8)

finForecast = open(sys.argv[2])
finActuals = open(sys.argv[3])

dateDayMaxs = []
dateDayMins = []
predictedMaxs = []
actualMaxs = []
predictedMins = []
actualMins = []

for forecastLine in finForecast[1:]:
    forecast = forecastLine.rstrip().split(',') # no '\n' at end
    # Time	fd0	fd1	fd2	fd3	fd4	fd5	fd6	fd7	fn0	fn1	fn2	fn3	fn4	fn5	fn6	fn7
    timeForecast = datetime.datetime.strptime(forecast[0], "%Y%m%d%H%M")
    timeActual = None
    actuals = None

    #get the corresponding actual temperature
    for actualsLine in finActuals[1:]:
        actuals = actualsLine.rstrip().split(',')
        # Time	Temp	t24maxtemp	t24mintemp
        timeActual = datetime.datetime.strptime(actuals[0], "%Y%m%d%H%M")
        
        # Check if this actual time corresponds to the forecasted time
        # ForecastDay + DaysOut == ActualDay
        if (timeForecast + datetime.timedelta(days=daysOut)).strftime('%d') == timeActual.strftime('%d'):
            break
    
    # if there's no max forecast data for this day, do nothing.
    
