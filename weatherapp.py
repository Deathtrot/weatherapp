#!/usr/bin/env python3

from flask import Flask, request, render_template
from urllib.parse import quote
import requests
import csv
import os

app = Flask(__name__)

weatherapi_key = os.environ.get('WEATHERKEY') #'e526e55a3248008806ffe0f40b17e68d'
timeapi_key = os.environ.get('TIMEKEY') #'MW80T0GA7P7A'
print(weatherapi_key, timeapi_key)

@app.route('/weather', methods=['GET', 'POST'])
def get_weather():
	if request.method == 'POST':
		city_name = request.form.get('city').title()
		city = quote(city_name)
		url = 'https://api.openweathermap.org/data/2.5/weather?q={query}&APPID={appid}&units=metric'.format(appid=weatherapi_key, query=city)
		print(url)
		response = requests.get(url)
		if response.status_code == 404:
			x = response.json()
			return x.get('message', 'sua irma')

		if response.status_code != 200:
			print(response.status_code, response.content)
			return "ERRO NÃO 200!"
				
		weather = response.json()
		print(weather)

		country = str(weather['sys']['country'])
		country_name = "placeholder"

		with open('codes.csv') as country_codes_csv:
			codes = csv.reader(country_codes_csv)
			for line in codes:
				if country in line:
					country_name = line[1]
					break

		max_temp = str(weather['main']['temp_max'])
		min_temp = str(weather['main']['temp_min'])
		curr_temp = str(weather['main']['temp'])
		latitude = str(weather['coord']['lat'])
		longitude = str(weather['coord']['lon'])

		timeurl = requests.get('http://api.timezonedb.com/v2/get-time-zone?key={}&format=json&by=position&lat={}&lng={}'.format(timeapi_key, latitude, longitude))
		time = timeurl.json()

		localtime = time['formatted']
		localtime = localtime.split(' ')
		localtime = localtime[1]
		#jdsguks
		#return render_template('response.html', city=city, country=country_name, localtime=localtime, curr_temp=curr_temp, min_temp=min_temp, max_temp=max_temp)
		return '<h1>{}</h1></br><h2>País: {}</h2></br><h2>Horário Local: {}</h2></br><h2>Temperatura Atual: {}°C</h2></br><h2>Temperatura Mínima: {}°C</h2></br><h2>Temperatura Máxima: {}°C</h2>'.format(city_name, country_name, localtime, curr_temp, min_temp, max_temp)

	return '<form method="POST"> Digite o nome de uma cidade em inglês: <input type="text" name="city"></br></br><input type="submit" value="Submit"></br></form>'

if __name__ == "__main__":
	app.run(debug=True, host='192.168.69.186', port='21180')