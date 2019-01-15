The aim of this application is to receive data on weather conditions at airports from an open source (http://tgftp.nws.noaa.gov/data/observations/metar/decoded/)
 and warn the user about adverse changes in weather conditions. The warning is issued in the form of an HTML report published using a web service.

Weather data for each airport are html pages with data about weather today. The data may be complete, and there may be a situation when some data is missing. 
We use regular expressions for parsing. We process each case, checking whether there is data or not, and comparing them with the threshold values. Then, we give the final result for the airport: the original data and the result of the test (corresponds to the threshold values or not).

In the "app" folder you can find the views.py file - it shows the parsing algorithm, inputs and outputs of the data.
init.py file aggregates the app, as a kind of сonfig.

To run the app you need virtual environment with such packages: requests, re, flask. 
To run the app use file run.py (don't forget to write the server address and port).