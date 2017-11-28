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

# Initialize an ElementTree
root = ET.fromstring(weatherXML)

# Extract the time layouts.
# We will store them in a dictionary for easy retrieval.
timelayouts = {}
# Use xpath to find the time-layout elements.
for timelayoutelement in root.findall("./data/time-layout"):
	# Get the layout key for each.
	layoutkey = timelayoutelement.find("layout-key").text
	# Retrieve and store the start times as a list.
	starttimes = []
	for starttimeelement in timelayoutelement.findall("start-valid-time"):
		starttimes.append(parse(starttimeelement.text))
	# Retrieve and store the start times as a list.
	endtimes = []
	for endtimeelement in timelayoutelement.findall("end-valid-time"):
		endtimes.append(parse(endtimeelement.text))
	# Store in the timelayouts dictionary.
	timelayouts[layoutkey] = [starttimes, endtimes]

highTimes = timelayouts['k-p24h-n7-2'][0]
lowTimes = timelayouts['k-p24h-n7-1'][0]
	
# Extract the weather parameters
# We will store them in a dictionary for easy retrieval.
weatherparameters = {}
for parameterelement in root.find("./data/parameters/."):
	# The tag name is a short name for the type of weather element.
	parameterelementtag = parameterelement.tag
	# The attributes are returned as a dictionary.
	parameterelementattribs = parameterelement.attrib
	# This name is better for use than the tag name since it is unique.
	parameterelementname = parameterelement.find("name").text
	if parameterelementtag == "temperature":
		# Retrieve and store the values as a list.
		parametervalues = []
		for value in parameterelement.findall("value"):
			parametervalues.append(value.text)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "values" : parametervalues}
	elif parameterelementtag == "conditions-icon":
		# Retrieve and store the values as a list.
		parametericonlinks = []
		for iconlink in parameterelement.findall("icon-link"):
			parametericonlinks.append(iconlink.text)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "iconlinks" : parametericonlinks}	
	elif parameterelementtag == "weather":
		# Retrieve and store the values as a list.
		parameterweatherconditions = []
		for weathercondition in parameterelement.findall("weather-conditions"):
			weathervalue = weathercondition.find("value")
			if weathervalue is None:
				weatherstr = "clear"
			else:
				weatherstr = weathervalue.attrib["coverage"] + " " + weathervalue.attrib["intensity"] + " " + weathervalue.attrib["weather-type"]
			parameterweatherconditions.append(weatherstr)
		# Store in the weatherparameters dictionary.
		weatherparameters[parameterelementname] = {"tag" : parameterelementtag , "attribs" : parameterelementattribs , "weatherconditions" : parameterweatherconditions}

#pp.pprint(weatherparameters)
#print len(weatherparameters)

maxTemps = weatherparameters["Daily Maximum Temperature"]["values"]
minTemps = weatherparameters["Daily Minimum Temperature"]["values"]

for ltim, mint, htim, maxt in zip(lowTimes, minTemps, highTimes, maxTemps):
	sys.stdout.write(ltim.strftime("%Y-%m-%d %H:%M:%S %z"))
	sys.stdout.write(", ")
	sys.stdout.write(mint)
	sys.stdout.write("\n")

	sys.stdout.write(htim.strftime("%Y-%m-%d %H:%M:%S %z"))
	sys.stdout.write(", ")
	sys.stdout.write(maxt)
	sys.stdout.write("\n")
