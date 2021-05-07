# Library imports

import requests, json
import datetime

# Dates

date_time = datetime.datetime.now()
day = Label(root, text = date_time.strftime('%A--'), bg='white', font=("bold", 15))
month_time = Label(root, text = date_time.strftime('%m %B'), bg='white', font=("bold", 15))

# Daytimes (hours)

time_hour = Label(root, text=dt.strftime('%I : %M %p'), bg='white', font=("bold", 15))

# Location research

name_city = StringVar()
input_city = Entry(root, textvariable = name_city, width=45)

def name_city():
    
    # Request API
    
    api_key = "12f04c87d16f8e311477842c595d4c77"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    request_weather_data = requests.get(base_url + input_city.get() + "&units=metric&appid=" + api_key)
    x = json.loads(request_weather_data.content)

    # Temp
    


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
