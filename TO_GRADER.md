# TO GRADER

This file contains the scripts that were used to complete the project.

* prob7.py
A variation of this file was used to get the forecast data and write it to a file.

* getStuff.py
This was used to get the forecast data, then was later edited to get the actual weather data.

* actuals_xmlToCsv.py
This was used to ingest the XML file that contained the actual temperature data.

* forecast_xmlToCsv.py
This was use to ingest all of the forecast XML files (Thank you globbing!) and put all the data into a CSV file.

* outFiles/
This contains all of the XML files that I harvested and many of the CSV files that I went through to come up with some useful data.

* outFiles/actualWeather2017-11-27 18:45:46.xml
This is the actual temperature data XML file that was harvested.

* outFiles/actuals.csv
This is the CSV file that was generated from the XML file above.

* outFiles/actuals_onlyMaxMins.csv
This file contains only the data I needed to do the plotting and run some statistics on the data.

* outFiles/webXml*.xml
These files all contain the forecast data.

* outFiles/forecasts2.csv
This is the CSV file that contained all the data from the forecast XML files. This was also used directly in plotting.

* plotter.py
This file is the one that was ran which plotted and ran statistics on the data. while in the outFiles directory, it can be run in the command line like so: python ../plotter.py 4 forecasts2.csv actuals_onlyMaxMins.csv

the 4 there represents how many days in the future the forecast was predicting.

