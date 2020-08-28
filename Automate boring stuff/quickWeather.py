# python 3
# -*- coding: utf-8 -*-
#program to take zip code and then retrive the temperature accordingly.
# Also adding sys argv to access command prompt as well as pyperclip for input options.
# plan is to expand the program to use zipcode, country, place name, lat&lon positions in the future.
# openweathermap.org api is being used. changes in api structure between book and current api will change things.
#free account only has access to current weather and so will not be able to print data for next 3 days
import os, pyperclip, requests, json, sys

os.system('cls')
while True:
    temperature = input('Enter F for temperature in Fahrenheit or C for celcius. Default is Kelvin: ')
    if temperature == 'F':
        units  = 'imperial'  
        tempind = u'\u2109'   
        windspeed = 'miles/hour'   
        break
    elif temperature == 'C':
        units = 'metric'  
        tempind = u'\u2103'  
        windspeed = 'meter/sec' 
        break
    else:
        units =  'Kelvin'   
        tempind = u'\u212A'  
        windspeed = 'meter/sec'
        break

while True:
    option = int(input('Do you want to enter location information (1) or zipcode (2) or latitude/longitude (3): '))
    if option == 1:
        city = input('Enter city state and country information (ex: Sanfransico,CA,US): ')  
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&cnt=3&units={units}&appid=10e2aea7c2852b4774fb5c9042507ce0'
        break
    elif option == 2:
        zipcode = input('Enter zipcode and country information (Ex: 16506,US): ')
        url = f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&cnt=3&&units={units}&appid=10e2aea7c2852b4774fb5c9042507ce0'
        break
    elif option == 3:
        lat = input('Enter Latitude position (ex: 37.17777): ')
        lon = input('Enter Longitude position (ex: -212.17777): ')
        url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&cnt=3&&units={units}&appid=10e2aea7c2852b4774fb5c9042507ce0'
    else:
        print('invalid entry. select 1 or 2 or 3')

print('getting the data from OpenWeatherMap.org....')
# Download the JSON data from OpenWeatherMap.org's API.

response =  requests.get(url)    
try:
    response.raise_for_status()
    print('Here is the weather info')
except ConnectionError:
    print(f'Error {response.status_code}. Unable to get the data')
    sys.exit()

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)
print(weatherData)
location = weatherData['name'] + ', ' + weatherData['sys']['country'] 
#print weather descriptions.
w = weatherData['weather']
print(f"current weather in {location}: {w[0]['main']} - {w[0]['description']} ")
print(f"current temperature is: {weatherData['main']['temp']}{tempind} ")
print(f"temperature feels like: {weatherData['main']['feels_like']}{tempind} ")
print (f"wind speed is  - {weatherData['wind']['speed']} { windspeed}")