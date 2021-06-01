# Library imports

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import json
import requests
import time, datetime
from requests import api

# Tkinter
root = Tk()
root.title("Weather-App")
root.geometry('960x540')
root.minsize("620","540")
root.maxsize("960","540")
root['background'] = "white"

# frames
input_frame = Frame(root)
weather_frame = Frame(root)
weathermap_frame = Frame(root)

input_frame.grid(row=1, column=0, columnspan=2, sticky=W)
weather_frame.grid(row=2, rowspan=2, column=0, columnspan=2, sticky=W)
weathermap_frame.grid(row=2, column=2)

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
    longitude = xcoord['lon']
    latitude = xcoord['lat']

    # Temp
    ytemp = api_result['main']
    temp_now = ytemp['temp']
    temp_Fahrenheit = (temp_now * 9 / 5) + 32
    weather_description = api_result['weather'][0]['main']
    humidity = ytemp['humidity']
    minimalTemp = ytemp['temp_min']
    maximalTemp = ytemp['temp_max']

    # Country (Bsp. Deutschland) + city(Bsp. Lörrach)
    z_api = api_result['sys']
    api_country = z_api['country']
    api_city = api_result['name']


# Searchbar + button for Location
city_search = Button(root, text="Search", command = name_city)
city_search.grid(row=1, column=1, padx=5, stick=W+E+N+S)



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
