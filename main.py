import json, requests
 
#Intro Welcome message
hello = input("Welcome to my Weather Program! -- Press Enter to Continue")

def weather_data(data):
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']
  
    print('Current Temperature : {} degrees fahrenheit'.format(temp))
    print('High Temperature : {} degrees fahrenheit'.format(hightemp))
    print('Low Temperature : {} degrees fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))