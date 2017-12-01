
import sys
import matplotlib.dates as mpldates

# We will use ElementTree to parse the XML
import xml.etree.ElementTree as ET
	
# We will use the following to parse the date strings.
from dateutil.parser import parse

# And this will be used to process date objects.
import datetime
import time

sys.stdout.write("Time,Temp,t24maxtemp,t24mintemp\n") 

for idx in range(len(sys.argv)):
	if idx == 0:
		continue
	try:
		tree = ET.parse(sys.argv[idx])
		root = tree.getroot()
	except IOError:
		print("no parse on " + sys.argv[idx])
		continue


	for node in root.findall("ob"):
		
		#start row with date
		timestr = "2017 " + node.attrib["time"]		
		
		dtTime = datetime.datetime.strptime(timestr, "%Y %d %b %I:%M %p")
		
		sys.stdout.write(dtTime.strftime("%Y%m%d%H%M"))

		sys.stdout.write(',')
		for variable in node:
			if variable.attrib["var"] == "T":
				sys.stdout.write(variable.attrib["value"])
			if variable.attrib["var"] == "T24MAX":
				sys.stdout.write(',')
				sys.stdout.write(variable.attrib["value"])
			if variable.attrib["var"] == "T24MIN":
				sys.stdout.write(',')
				sys.stdout.write(variable.attrib["value"])
		sys.stdout.write('\n')
			
				
