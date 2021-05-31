from tkinter import *
from PIL import ImageTk, Image
import json
import requests
import time
from requests import api

# root details
root = Tk()
root.title("Weather-App")
root.geometry('960x540')

# frames
input_frame = Frame(root)
weather_frame = Frame(root)
weathermap_frame = Frame(root)

input_frame.grid(row=1, column=0, columnspan=2, sticky=W)
weather_frame.grid(row=2, rowspan=2, column=0, columnspan=2, sticky=W)
weathermap_frame.grid(row=2, column=2)

api_key = "12f04c87d16f8e311477842c595d4c77"

# functions

def celsius_Fahrenheit_converter():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    main = api['main']  # temperatures and humidity

    #Celsius
    if(Converter['text'] == "C°"):
        Converter['text'] = 'F°'
        temp.configure(text=str(main['temp']) + "°C")
        temp_max.configure(text="max. " + str(main["temp_max"]) + "°C")
        temp_min.configure(text="min. " + str(main["temp_min"]) + "°C")
        humidity.configure(text="humidity: " + str(main['humidity']) + "%")

    else:
    #Fahrenheit
        Converter['text'] = 'C°'
        temp_Fahrenheit = round(((main['temp'] * 9 / 5) + 32), 2)
        temp.configure(text=str(temp_Fahrenheit) + "°F")
        temp_max_Fahrenheit = round(((main["temp_max"] * 9 / 5) + 32),2)
        temp_max.configure(text="max. " + str(temp_max_Fahrenheit) + "°F")
        temp_min_Fahrenheit = round(((main["temp_min"] * 9 / 5) + 32),2)
        temp_min.configure(text="min. " + str(temp_min_Fahrenheit) + "°F")
        humidity.configure(text="humidity: " + str(main['humidity']) + "%")

# click - event (for Placeholder in Searchbar)

def click(event):
    if(inpt['state'] == DISABLED):
        inpt.config(state = NORMAL)
        inpt.delete(0, END)

# city search function
def search_city(event=None):
    # set city label
    if city_name.get() != "":
        city_print.set(city_name.get())

    # API call
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)

    api = json.loads(api_request.content)
    main = api['main']  # temperatures and humidity
    weather = api['weather']  # cloudy/sunny etc.

    # weather cofiguration
    temp.configure(text=str(main['temp']) + "°C")
    temp_max.configure(text="max. " + str(main["temp_max"]) + "°C")
    temp_min.configure(text="min. " + str(main["temp_min"]) + "°C")
    humidity.configure(text="humidity: " + str(main['humidity']) + "%")

# ----------------- HIER NOCH PROBLEME

def weather_forecast():
    test = api.get()
    xcoord = test['coord']
    longtitude = xcoord['lon']
    latitude = xcoord['lat']
    forecast_request = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={"
    + latitude + "}&lon={" + longtitude + "}&dt={" + time + "}&appid={" + api_key + "}")

# ----------------- HIER NOCH PROBLEME

# Image
img = ImageTk.PhotoImage(Image.open("Logo_Python.png"))
logo = Label(root, pady=100, image=img)
logo.grid(row=0, column=0, sticky=W)

# city input
input_label = Label(input_frame, text="Name:")

city_name = StringVar()
city_name.set("Search for your city!")
inpt = Entry(input_frame, width=50, textvariable=city_name)
inpt.bind("<Return>", search_city)  # bind function to ENTER
inpt.config(state=DISABLED)
inpt.bind("<Button-1>",click)
input_button = Button(input_frame, text="search",
                      command=search_city)

input_label.grid(row=0, column=1, sticky=W, padx=10, pady=5)
inpt.grid(row=0, column=2, sticky=E, padx=10, pady=5)
input_button.grid(row=0, column=3, sticky=E, pady=2.5)

# weather
city_print = StringVar()

label_city = Label(weather_frame, textvariable=city_print, font=("bold", 25))

temp = Label(weather_frame, padx=10, pady=5, font=("bold", 20))

temp_max = Label(weather_frame, padx=10, pady=0)

temp_min = Label(weather_frame, padx=10, pady=0)

humidity = Label(weather_frame, padx=10, pady=10)

Converter = Button(input_frame, text = "F°", command = celsius_Fahrenheit_converter)
Converter.grid(row=0, column=4, sticky=E, pady=2.5)

label_city.grid(row=1, column=0, sticky=W, padx=10, pady=10)
temp.grid(row=2, column=0, sticky=W)
temp_max.grid(row=3, column=0, sticky=W)
temp_min.grid(row=4, column=0, sticky=W)
humidity.grid(row=5, column=0, sticky=W)

# weather prediction
Unix_time_now = int(time.time())


# XXX.place(relx=1.0, rely=1.0, x=0, y=0, anchor=S+E)


# start window
root.mainloop()

