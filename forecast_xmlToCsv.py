######################
# GetNDFDWeather7.py
######################

import sys
import matplotlib.dates as mpldates

# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET
    
# We will use the following to parse the date strings.
from dateutil.parser import parse

# And this will be used to process date objects.
import datetime
import time

sys.stdout.write("Time,fd0,fd1,fd2,fd3,fd4,fd5,fd6,fd7,fn0,fn1,fn2,fn3,fn4,fn5,fn6,fn7\n") 

for idx in range(len(sys.argv)):
    if idx == 0:
        continue
    try:
        tree = ET.parse(sys.argv[idx])
        root = tree.getroot()
    except IOError:
        print("no parse on " + sys.argv[idx])
        continue

    #start row with date
    dtTime = datetime.datetime.strptime(sys.argv[idx], "webXml%Y-%m-%d %H:%M:%S.xml")
    sys.stdout.write(dtTime.strftime("%Y%m%d%H%M"))

    ##########################################################
    # Get the time stamps from the file
    ##########################################################
    timesFromXml = []
    try:
        layouts = root.find("data").findall("time-layout")
    except AttributeError:
        sys.stdout.write(",,,,,,,,,,,,,,,,\n")
        continue
    
    for layout in layouts:
        if "p3h" in layout.find("layout-key").text:
            continue
        
        time = layout.find("start-valid-time")
        # Take stuff before the "-"
        timeTime = time.text[0:19]
        timeFromLayout = datetime.datetime.strptime(timeTime, "%Y-%m-%dT%H:%M:%S")
        timesFromXml.append(timeFromLayout)

    ###################################################
    # Print out the times
    ###################################################
    tempsFromXml = []
    try:
        temps = root.find("data").find("parameters").findall("temperature")
    except AttributeError:
        sys.stdout.write(",,,,,,,,,,,,,,,,\n")
        continue

    for idxTemps in range(len(temps)):
        sameDay = False
        if temps[idxTemps].get('type') == 'hourly':
            continue

        # find out if they are the same day.
        if dtTime.strftime("%d") == timesFromXml[idxTemps].strftime("%d"):
            sameDay = True


        # do printing
        if not sameDay:
            sys.stdout.write(",")
        vals = temps[idxTemps].findall("value")
        for idxVals in range(7):
            sys.stdout.write(",")
            if idxVals < len(vals):
                sys.stdout.write(vals[idxVals].text)
        if sameDay:
            sys.stdout.write(",")
    sys.stdout.write("\n")

