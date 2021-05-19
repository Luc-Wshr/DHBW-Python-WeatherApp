from tkinter import *
from PIL import ImageTk, Image
import json
import requests


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


# functions
def search_city(event=None):
    # set city label
    if city_name.get() != "Search for your city!":
        city_print.set(city_name.get())

    # API call

    api_key = "12f04c87d16f8e311477842c595d4c77"
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)

    api = json.loads(api_request.content)
    main = api['main']  # temperatures and humidity
    weather = api['weather']  # cloudy/sunny etc.

    # weather cofiguration
    temp.configure(text=str(main['temp']) + "°")
    temp_max.configure(text="max. " + str(main["temp_max"]) + "°")
    temp_min.configure(text="min. " + str(main["temp_min"]) + "°")
    humidity.configure(text="humidity: " + str(main['humidity']) + "%")


# Image
img = ImageTk.PhotoImage(Image.open("Logo_Python.png"))
logo = Label(root, pady=100, image=img)
logo.grid(row=0, column=0, sticky=W)

# city input
input_label = Label(input_frame, text="INPUT:")

city_name = StringVar()
city_name.set("Search for your city!")
inpt = Entry(input_frame, width=50, textvariable=city_name)
inpt.bind("<Return>", search_city)  # bind function to ENTER

input_button = Button(input_frame, text="search",
                      command=search_city)

input_label.grid(row=0, column=1, sticky=W, padx=10, pady=5)
inpt.grid(row=0, column=2, sticky=E, padx=10, pady=5)
input_button.grid(row=0, column=3, sticky=E, pady=2.5)

# weather
city_print = StringVar()
label_city = Label(weather_frame, textvariable=city_print, font=("bold", 25))

temp = Label(weather_frame, padx=10, pady=5, font=(15))

temp_max = Label(
    weather_frame, padx=10, pady=0)  # autoformatter!?

temp_min = Label(
    weather_frame, padx=10, pady=0)

humidity = Label(weather_frame, padx=10, pady=10)

label_city.grid(row=1, column=0, sticky=W, padx=10, pady=10)
temp.grid(row=2, column=0, sticky=W)
temp_max.grid(row=3, column=0, sticky=W)
temp_min.grid(row=4, column=0, sticky=W)
humidity.grid(row=5, column=0, sticky=W)

# weather map
weathermap_img = ImageTk.PhotoImage(Image.open("map.png"))
weathermap = Label(root, image=weathermap_img)
weathermap.place(relx=1.0, rely=1.0, x=0, y=0, anchor=S+E)


# start window
root.mainloop()
