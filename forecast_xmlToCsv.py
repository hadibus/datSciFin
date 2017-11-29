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

sys.stdout.write("Time,fd1,fd2,fd3,fd4,fd5,fd6,fd7,fn1,fn2,fn3,fn4,fn5,fn6,fn7\n") 

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

	try:
		temps = root.find("data").find("parameters").findall("temperature")
	except AttributeError:
		sys.stdout.write(",,,,,,,,,,,,,,\n")
		continue
	for temp in temps:
		if temp.get('type') == 'hourly':
			continue
		vals = temp.findall("value")
		for idxVals in range(7):
			sys.stdout.write(",")
			if idxVals < len(vals):
				sys.stdout.write(vals[idxVals].text)
	sys.stdout.write("\n")

