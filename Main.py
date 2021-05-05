import requests, json

api_key = "3a5ee960a96dd608673bce4a6288a65c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("From where do you want to know the weather? : ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
  
get_responses = response.json()

if get_responses["cod"] != "404":
    y = get_responses["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]
    z = get_responses["weather"]
    weather_description = z[0]["description"]

    print(" Temperatur (in kelvin) = " +
                    str(current_temperature) + 
          "\n Atmosphärischer Druck (in hPa = " +
                    str(current_pressure) +
          "\n Feuchtigkeit (in %) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))
  
else:
    print(" City Not Found ")
