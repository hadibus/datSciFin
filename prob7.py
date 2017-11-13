import datetime
import sys
import time
# We will use the request package to make http requests.
import requests

# Set now and the next time
nextTime = nowTime = datetime.datetime.now()


# Set the end time
endTime = nowTime + datetime.timedelta(days=2)

print("This program will run for two days.")
print("It saves a xml file every 15 minutes.")
print("A dot prints every 30 seconds")
print("Starting now.")

while nowTime < endTime:
	while nowTime < nextTime:
		time.sleep(10)
		nowTime = datetime.datetime.now()
	sys.stdout.write("\n")

	requeststr = "https://graphical.weather.gov/xml/sample_products/browser_interface/ndfdXMLclient.php?lat=40.4385&lon=-79.9973&product=time-series&maxt=maxt&mint=mint&icons=icons&wx=wx"
	weatherXML = requests.get(requeststr).text
	nextTime = nextTime + datetime.timedelta(minutes=15)

	filestr = "webXml" + nowTime.strftime("%Y-%m-%d %H:%M:%S") + ".xml"

	print("Writing to: " + filestr + " now...")
	with open(filestr, "w") as fout:
		fout.write(weatherXML)
	print("Done writing to " + filestr)
	
	

