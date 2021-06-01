#----------------------------------------------------------------------------------------Library imports
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import json
import requests
import time
from requests import api
from tkinter import messagebox
#----------------------------------------------------------------------------------------root details
root = Tk()
root.title("Weather-App")
root.geometry('960x540')
root.minsize("620","540")
root.maxsize("960","540")

#----------------------------------------------------------------------------------------frames
input_frame = Frame(root)
weather_frame = Frame(root)
weathermap_frame = Frame(root)

weather_frame['background']="light grey"
input_frame.grid(row=1, column=0, columnspan=2, sticky=W)
weather_frame.grid(row=2, rowspan=2, column=0, columnspan=2, sticky=W)
weathermap_frame.grid(row=2, column=2)
#----------------------------------------------------------------------------------------Key-values
api_key = "12f04c87d16f8e311477842c595d4c77"
countryName = StringVar()
Flagge = StringVar()
#------------------------------------------------------------------------------------------------------------functions
def celsius_Fahrenheit_converter():
    """This function converts the Temperature of the selected Location from Celsius to Fahrenheit and vice-versa """

    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    main = api['main']  # temperatures and humidity
    #------------------------------------------------------------------Celsius
    if(Converter['text'] == "C°"):
        Converter['text'] = 'F°'
        temp.configure(text=str(main['temp']) + "°C")
        temp_max.configure(text="max. " + str(main["temp_max"]) + "°C")
        temp_min.configure(text="min. " + str(main["temp_min"]) + "°C")
        humidity.configure(text="humidity: " + str(main['humidity']) + "%")
    else:
    #------------------------------------------------------------------Fahrenheit
        Converter['text'] = 'C°'
        temp_Fahrenheit = round(((main['temp'] * 9 / 5) + 32), 2)
        temp.configure(text=str(temp_Fahrenheit) + "°F")
        temp_max_Fahrenheit = round(((main["temp_max"] * 9 / 5) + 32),2)
        temp_max.configure(text="max. " + str(temp_max_Fahrenheit) + "°F")
        temp_min_Fahrenheit = round(((main["temp_min"] * 9 / 5) + 32),2)
        temp_min.configure(text="min. " + str(temp_min_Fahrenheit) + "°F")
        humidity.configure(text="humidity: " + str(main['humidity']) + "%")
        
#----------------------------------------------------------------------------------------Hour-clock
def get_time():
    """This function gets the current Time and displays it in Hour-Minute-Second in American Time AM/PM"""
    timeVar = time.strftime("%I:%M:%S %p")
    label_clock.config(text=timeVar)
    label_clock.after(200, get_time)

#----------------------------------------------------------------------------------------click-event
def click(event):
    """This function makes a Placeholder text for the City-Searchfield"""
    if(inpt['state'] == DISABLED):
        inpt.config(state = NORMAL)
        inpt.delete(0, END)

#----------------------------------------------------------------------------------------city-search-function
def search_city(event=None):
    """This function searches a selected city on openweathermap.org and requests the weatherdata via API"""
    #------------------------------------------------------------------set city label
    if city_name.get() != "":
        city_print.set(city_name.get())

    #------------------------------------------------------------------API call
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    if api['cod'] != '404':
        main = api['main']
        weather = api['weather']
        #------------------------------------------------------------------fetch-and-download-flag-image
        z_api = api['sys']
        api_country = z_api['country']
        country_flag_image = requests.get("https://www.countryflags.io/"+ api_country +"/flat/64.png")
        img_data = open(("Flags/"+api_country+".png"), "wb")
        img_data.write(country_flag_image.content)
        img_data.close()
        countryName.set(api_country)
        #------------------------------------------------------------------set flag image
        flag_adress= ImageTk.PhotoImage(Image.open("Flags/"+api_country +".png"))
        flag_img = Image.open("Flags/"+api_country +".png")
        loaded_img = ImageTk.PhotoImage(flag_img)
        Flag_label = tkinter.Label(image=loaded_img)
        Flag_label.image = loaded_img
        Flag_label.grid(row=0, column=1, sticky=W)
        label_flag = Label(root, pady=100, image=flag_adress)
        label_flag.grid(row=0, column=2, sticky=W)

        #------------------------------------------------------------------write Weather data into Labels
        weather_today = weather[0]['main']
        if(weather_today == 'Rain'):
            messagebox.showwarning("Weather forecast","Take an umbrella with you today! it's going to rain")

        #------------------------------------------------------------------Weather-Notifications
        temp.configure(text=str(main['temp']) + "°C")
        temp_max.configure(text="max. " + str(main["temp_max"]) + "°C")
        temp_min.configure(text="min. " + str(main["temp_min"]) + "°C")
        humidity.configure(text="humidity: " + str(main['humidity']) + "%")
        weather_description.configure(text=weather_today)
        inpt.config(state=DISABLED)
    else:
        countryName.set(" City not found")

#----------------------------------------------------------------------------------------Weather forecast
def weather_forecast():
    """This function gets the Weather forecast for the next few days"""
    test = api.get()
    xcoord = test['coord']
    longtitude = xcoord['lon']
    latitude = xcoord['lat']
    forecast_request = requests.get("https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={"
    + latitude + "}&lon={" + longtitude + "}&dt={" + time + "}&appid={" + api_key + "}")

#----------------------------------------------------------------------------------------set Favourites for standart-view on startup
def save_as_favorite():
    """This function saves a Favourite to a json file to have it as Standart startup"""
    filePathName = 'Code/settings/fav.json'
    fav_Name = { "favourite" : city_name.get()}
    with open(filePathName, 'w') as fp:
        json.dump(fav_Name, fp)


#----------------------------------------------------------------------------------------Image
img = ImageTk.PhotoImage(Image.open("Logo_Python.png"))
logo = Label(root, pady=100, image=img)
logo.grid(row=0, column=0, sticky=W)

#----------------------------------------------------------------------------------------city input
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

#----------------------------------------------------------------------------------------weather
city_print = StringVar()
label_country = Label(weather_frame, textvariable=countryName, font=("bold", 25),bg="light grey")
label_clock = Label(root, font=("Calibri",20), bg="grey",fg="white")
label_city = Label(weather_frame, textvariable=city_print, font=("bold", 25),bg="light grey")
temp = Label(weather_frame, padx=10, pady=5, font=("bold", 20),bg="light grey")
weather_description = Label(weather_frame, padx=10, pady=5, font=("Calibri",15),bg="light grey")
temp_max = Label(weather_frame, padx=10, pady=0, font=("Calibri", 10),bg="light grey")
temp_min = Label(weather_frame, padx=10, pady=0, font=("Calibri", 10),bg="light grey")
humidity = Label(weather_frame, padx=10, pady=10, font=("Calibri", 10),bg="light grey")
Converter = Button(input_frame, text = "F°", command = celsius_Fahrenheit_converter)
Favourites = Button(input_frame, text = "✰", command = save_as_favorite )

weather_description.grid(row=2, column=1, sticky=W)
label_country.grid(row =1, column =2, sticky = E, pady = 2.5 , padx = 10)
label_clock.grid(row=0, column=5, sticky=N, pady=2.5,padx=20)
Converter.grid(row=0, column=4, sticky=E, pady=2.5, padx=25)
Favourites.grid(row=0, column=5, sticky=E, pady=2.5, padx=15)
label_city.grid(row=1, column=0, sticky=W, padx=10, pady=10)
temp.grid(row=2, column=0, sticky=W)
temp_max.grid(row=3, column=0, sticky=W)
temp_min.grid(row=4, column=0, sticky=W)
humidity.grid(row=5, column=0, sticky=W)

#----------------------------------------------------------------------------------------load Settings.json
with open('Code/settings/fav.json') as f:
    fav = json.load(f)
    preload = fav['favourite']
    city_name.set(preload)
    search_city()

#----------------------------------------------------------------------------------------weather prediction
Unix_time_now = int(time.time())

get_time()

#----------------------------------------------------------------------------------------start window
root.mainloop()

