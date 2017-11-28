import datetime
import sys
import time
# We will use the request package to make http requests.
import requests

nowTime = datetime.datetime.now()

requeststr = "http://www.wrh.noaa.gov/mesowest/getobextXml.php?sid=KAGC&num=500"
weatherXML = requests.get(requeststr).text

filestr = "actualWeather" + nowTime.strftime("%Y-%m-%d %H:%M:%S") + ".xml"

print("Writing to: " + filestr + " now...")
with open(filestr, "w") as fout:
	fout.write(weatherXML)
print("Done writing to " + filestr)
	
	

