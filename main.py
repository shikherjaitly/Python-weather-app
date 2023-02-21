import os
import requests
from datetime import datetime 

api_key = os.environ['weather_api_key']
location = input("Enter City Name: ")
#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

api_link= requests.get(complete_api_link)
api_data = api_link.json()


if api_data['cod'] == '404':
    print("Invalid City {}: Please check city name:".format(location))

else:
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_description = (api_data['weather'][0]['description'])
    humidity = (api_data['main']['humidity'])
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


    print("---------------------------")
    print("Weather Status for - {} || {}".format(location.upper(), date_time))

    print("Current Temperature is: {:.2f} deg C".format(temp_city))
    print("Current Humidity is: {}".format(humidity),"%")
