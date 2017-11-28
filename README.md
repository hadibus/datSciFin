# datSciFin
final project data science

For the output files there are those that are forecast temperatures, and those that are actual temperatures.

The files that are forecast data are entitled xml

The file that contains the actual temperatures is entitled actual

###############################################################
# Format of the xml forecast data
###############################################################

k-p24h-n7-1 refers to forecasts that are 24 hours apart and there are seven of them.
	you can tell because they begin at 7:00 and end at 19:00

k-p24h-n7-2 does the same, but for night time. They start at 19:00 and end at 8:00.

k-p3h-n39-3 refers to forecasts that are 3 hours apart and there are 39 of them.

Below there are temperature sections. they show the max and min temperature forecasts
	according to their time layouts. those layouts are "k-p24h-n7-1", "k-p24h-n7-2", and 
	"k-p3h-n39-3". 

##############################################################
# Format of the actual temperature data
##############################################################

There are a list of time objects. inside these time objects, there are several pieces of
useful data. It looks like the important one is the temperature, and the 24 hour max and min.

Actually, it looks like the 24 hour min and max temperatures are what are important.


#############################################################
# Plan
#############################################################

For each distance of forecast days:
	plot the following...
	For each webXml file:
		plot the forecast vs the actual
		-OR-
		plot the absolute value of the difference.

What about plotting both the 24hr min and max on the same graphs. Then there would only
be 7 graphs. I like that!
