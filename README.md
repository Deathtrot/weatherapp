# weatherapp
Python project using Flask and Requests to send queries to APIs and show results

====

Welcome!

This is a Python script I made for learning purposes. It works sending queries to both OpenWeatherMap and TimezoneDB to show the current, maximum and minimum temperature and local time for any city in the world, selected by the user. It also shows the country in which the selected city is located.

Put both weatherapp.py and codes.csv files in the same folders. The .csv file is responsible for converting the country code sent by the API (which is a two letter standard ISO code) into the full lenght name. Set the Flask server with the startweatherapp.sh file and open the localhost in your web browser, using the PORT 21180. A simple HTML will prompt the user for a city name and the response will be printed.
