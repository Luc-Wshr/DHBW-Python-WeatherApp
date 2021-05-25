# Library imports

from tkinter import *
import requests, json
import datetime

# Tkinter

root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

# Dates

date_time = datetime.datetime.now()
day = Label(root, text = date_time.strftime('%A--'))
month_time = Label(root, text = date_time.strftime('%m %B'))

# Daytimes (hours)

time_hour = Label(root, text=date_time.strftime('%I : %M %p'))

# Location research

name_city = StringVar()
input_city = Entry(root, textvariable = name_city, width=45)

def name_city():
    
    # Request API
    api_key = "12f04c87d16f8e311477842c595d4c77"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    request_weather_data = requests.get(base_url + input_city.get() + "&units=metric&appid=" + api_key)
    api_result = json.loads(request_weather_data.content)

    # Coordinates long, lat
    xcoord = api_result['coord']
    longtitude = xcoord['lon']
    latitude = xcoord['lat']

    # Temp
    ytemp = api_result['main']
    temp_now = ytemp['temp']
    humidity = ytemp['humidity']
    minimalTemp = ytemp['temp_min']
    maximalTemp = ytemp['temp_max']

    # Country (Bsp. Deutschland) + city(Bsp. Lörrach)
    z_api = api_result['sys']
    api_country = z_api['country']
    api_city = api_result['name']


root.mainloop()

""" /------ Auskommentiert ---------/

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
  
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
  
else:
    print(" City Not Found ")
"""
