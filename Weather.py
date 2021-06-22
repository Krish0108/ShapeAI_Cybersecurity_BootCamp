import requests
from datetime import datetime

api_key = '0d175f1b6fce6d983d9bf8304a033a23'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")
print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc.capitalize())
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

with open('Weather.txt', 'w') as f:
    f.write("------------------------------------------------------------- \n")
    f.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
    f.write("------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
    f.write("Current weather desc  : {} \n".format(weather_desc.capitalize()))
    f.write("Current Humidity      : {} % \n".format(hmdt))
    f.write("Current wind speed    : {} kmph \n".format(wind_spd))