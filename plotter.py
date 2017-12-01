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
import matplotlib.patches as mpatches
from math import sqrt

daysOut = int(sys.argv[1])
assert(daysOut > -1 and daysOut < 8)

finForecast = open(sys.argv[2])
finActuals = open(sys.argv[3])

dateDayMaxs = []
predictedMaxs = []
actualMaxs = []

dateDayMins = []
predictedMins = []
actualMins = []

headerPassed = False
firstTimeFlag = False
firstTime = None

maxErr = []
minErr = []

for forecastLine in finForecast:
    # Skip the header
    if not headerPassed:
        headerPassed = True
        continue
    forecast = forecastLine.rstrip().split(',') # no '\n' at end
    # Time	fd0	fd1	fd2	fd3	fd4	fd5	fd6	fd7	fn0	fn1	fn2	fn3	fn4	fn5	fn6	fn7
    timeForecast = datetime.datetime.strptime(forecast[0], "%Y%m%d%H%M")
    if not firstTimeFlag:
        firstTimeFlag = True
        firstTime = timeForecast
    timeActual = None
    actuals = None

    #get the corresponding actual temperature
    headerPassedInner = False
    finActuals.seek(0) # GO back to beginning!
    for actualsLine in finActuals:
        # Skip the header
        if not headerPassedInner:
            headerPassedInner = True
            continue
        actuals = actualsLine.rstrip().split(',')
        # Time	Temp	t24maxtemp	t24mintemp
        timeActual = datetime.datetime.strptime(actuals[0], "%Y%m%d%H%M")
        
        # Check if this actual time corresponds to the forecasted time
        # ForecastDay + DaysOut == ActualDay
        if (timeForecast + datetime.timedelta(days=daysOut)).strftime('%d') == timeActual.strftime('%d'):
            break
    
    # if there's no max forecast data for this day, do nothing.
    # daysOut
    if forecast[1 + daysOut] != '':
        t = timeForecast - firstTime + datetime.timedelta(days=daysOut)
        dateDayMaxs.append(int((t.days * 1440) + (t.seconds / 60)))
        predictedMaxs.append(int(forecast[1 + daysOut]))
        actualMaxs.append(int(actuals[2])) # idx 2 is maxs
        maxErr.append(abs(int(forecast[1 + daysOut]) - int(actuals[2])))

    # If there's no min forecast data for this day, do nothing.
    if forecast[1 + 8 + daysOut] != '':
        t = timeForecast - firstTime + datetime.timedelta(days=daysOut)
        dateDayMins.append(int((t.days * 1440) + (t.seconds / 60)))
        predictedMins.append(int(forecast[1 + 8 + daysOut]))
        actualMins.append(int(actuals[3])) # idx 3 is mins
        minErr.append(abs(int(forecast[1 + 8 + daysOut]) - int(actuals[3])))

#print(dateDayMaxs)
plt.plot(dateDayMaxs, predictedMaxs, "g")
plt.plot(dateDayMaxs, actualMaxs, "r")
green_patch = mpatches.Patch(color='green', label='Predicted')
red_patch = mpatches.Patch(color='red', label='Actual')
plt.ylabel("Temperature (F)")
plt.xlabel("Relative Time in Minutes")
plt.title("Day Forecast Accuracy (" + str(daysOut) + " days out)")
plt.legend(handles=[green_patch, red_patch])

plt.show()

#print avg err
maxAvgErr = sum(maxErr) / len(maxErr)
print("Max AVG ERR: " + str(maxAvgErr))
diffs = [i - maxAvgErr for i in maxErr]
stdDev = sqrt(sum([i**2 for i in diffs]) / len(maxErr))
print("Max STD DEV: " + str(stdDev))

plt.plot(dateDayMins, predictedMins, "g")
plt.plot(dateDayMins, actualMins, "r")
plt.legend(handles=[green_patch, red_patch])
plt.ylabel("Temperature (F)")
plt.xlabel("Relative Time in Minutes")
plt.title("Night Forecast Accuracy (" + str(daysOut) + " days out)")
plt.show()

minAvgErr = sum(minErr) / len(minErr)
print("Min AVG ERR: " + str(minAvgErr))
diffs = [i - minAvgErr for i in minErr]
stdDev = sqrt(sum([i**2 for i in diffs]) / len(minErr))
print("Min STD DEV: " + str(stdDev))