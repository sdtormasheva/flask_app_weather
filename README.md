The aim of this application is to receive data on weather conditions at airports from an open source (http://tgftp.nws.noaa.gov/data/observations/metar/decoded/)
 and warn the user about adverse changes in weather conditions. The warning is issued in the form of an HTML report published using a web service.

In the "app" folder you can find the views.py file - it shows the parsing algorithm, inputs and outputs of the data.
init.py file aggregates the app, as a kind of сonfig.

To run the app you need virtual environment with such packages: requests, re, flask. 
To run the app use file run.py (don't forget to write the server address and port).