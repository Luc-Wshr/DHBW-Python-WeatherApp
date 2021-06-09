#----------------------------------------------------------------------------------------Library imports
from tkinter import *
from PIL import ImageTk, Image
from datetime import date, timedelta
from requests import api
from tkinter import messagebox
import tkinter,json, requests, time

#----------------------------------------------------------------------------------------root details
root = Tk()
root.title("Weather-App")
root.geometry('960x540')
root.minsize("620","540")
root.maxsize("960","540")

#----------------------------------------------------------------------------------------frames
input_frame = Frame(root)
date_time_frame = Frame(root)
weather_frame = Frame(root)
eight_day_forecast_frame = Frame(root)
weathermap_frame = Frame(root)

weather_frame['background']="light grey"



input_frame.grid(row=0, column=1)
date_time_frame.grid(row=0, column=6, sticky=E)
weather_frame.grid(row=1, rowspan=7, column=0, columnspan=3, sticky=W)
eight_day_forecast_frame.grid(row=1, rowspan=9, column=4, columnspan=3, sticky=E)
weathermap_frame.grid(row=2, column=2)
#----------------------------------------------------------------------------------------Key-values
api_key = "12f04c87d16f8e311477842c595d4c77"
countryName = StringVar()

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
    Date_today = date.today()
    label_date.config(text=Date_today)
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
        flag_img = Image.open("Flags/"+api_country +".png")
        loaded_img = ImageTk.PhotoImage(flag_img)
        Flag_label = tkinter.Label(weather_frame, image=loaded_img, bg="light grey")
        Flag_label.image = loaded_img
        Flag_label.grid(row=0, column=2, sticky=E)

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
        eight_day_forecast()
        inpt.config(state=DISABLED)
    else:
        city_print.set(" City not found")

#----------------------------------------------------------------------------------------8 Day Weather Forecast
def eight_day_forecast():
    """this function gives Information about the max. and min. temperature and weather description for the next 8 days (today included)"""
    api_request_city = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)
    api_city = json.loads(api_request_city.content)
    location_x = api_city["coord"]["lon"]
    location_y = api_city["coord"]["lat"]

    api_request_forecast = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location_y) + "&lon=" + str(location_x) + "&exclude=current,minutely,hourly&appid=" +api_key)
    api = json.loads(api_request_forecast.content)
    weekdays = {
        0:"Mon",
        1:"Tue",
        2:"Wed",
        3:"Thu",
        4:"Fri",
        5:"Sat",
        6:"Sun"
    }
    months = {
        1:"Jan",
        2:"Feb",
        3:"Mar",
        4:"Apr",
        5:"May",
        6:"Jun",
        7:"Jul",
        8:"Aug",
        9:"Sep",
        10:"Oct",
        11:"Nov",
        12:"Dec",
    }
    today = date.today()
    today_month = today.month
    today_day = today.day
    today_weekday = today.weekday()
    days = []
    for i in range(7):
        tdelta = timedelta(days=1 + i)
        new_time = today + tdelta
        new_time_day = new_time.day
        days.append(new_time_day)
    #icon = requests.get("http://openweathermap.org/img/wn/" + api["daily"][0]["weather"][0]["icon"] + "@2x.png")
    #icon_data = open(("Icons/"+api["daily"][0]["weather"][0]["icon"]+".png"), "wb")
    #icon_data.write(icon.content)
    #icon_data.close()
    #icon_adress= ImageTk.PhotoImage(Image.open("Icons/"+api["daily"][0]["weather"][0]["icon"] +".png"))
    #icon_img = Image.open("Icons/"+api["daily"][0]["weather"][0]["icon"] +".png")
    #loaded_img = ImageTk.PhotoImage(icon_img)
    #Icon_label = tkinter.Label(image=loaded_img)
    #Icon_label.image = loaded_img
    

    label_day_one.configure(text=str(weekdays[today_weekday]) + ", " + str(months[today_month]) + " " + str(today_day) + "    " +
                            str(round(api["daily"][0]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][0]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][0]["weather"][0]["description"])
    label_day_two.configure(text=str(weekdays[(today_weekday + 1) % 7]) + ", " + str(months[today_month]) + " " + str(days[0]) + "    " +
                            str(round(api["daily"][1]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][1]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][1]["weather"][0]["description"])
    label_day_three.configure(text=str(weekdays[(today_weekday + 2) % 7]) + ", " + str(months[today_month]) + " " + str(days[1]) + "    " +
                            str(round(api["daily"][2]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][2]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][2]["weather"][0]["description"])
    label_day_four.configure(text=str(weekdays[(today_weekday + 3) % 7]) + ", " + str(months[today_month]) + " " + str(days[2]) + "    " +
                            str(round(api["daily"][3]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][3]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][3]["weather"][0]["description"])
    label_day_five.configure(text=str(weekdays[(today_weekday + 4) % 7]) + ", " + str(months[today_month]) + " " + str(days[3]) + "    " +
                            str(round(api["daily"][4]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][4]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][4]["weather"][0]["description"])
    label_day_six.configure(text=str(weekdays[(today_weekday + 5) % 7]) + ", " + str(months[today_month]) + " " + str(days[4]) + "    " +
                            str(round(api["daily"][5]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][5]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][5]["weather"][0]["description"])
    label_day_seven.configure(text=str(weekdays[(today_weekday + 6) % 7]) + ", " + str(months[today_month]) + " " + str(days[5]) + "    " +
                            str(round(api["daily"][6]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][6]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][6]["weather"][0]["description"])
    label_day_eight.configure(text=str(weekdays[(today_weekday + 7) % 7]) + ", " + str(months[today_month]) + " " + str(days[6]) + "    " +
                            str(round(api["daily"][7]["temp"]["max"] - 273.13)) + "/" + str(round(api["daily"][7]["temp"]["min"] - 273.13)) 
                            + "°C     " + api["daily"][7]["weather"][0]["description"])

#---------------------------------------------------------------------------------------Weather map
def weather_map():
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_name.get() + "&units=metric&appid="+api_key)
    api = json.loads(api_request.content)
    location_x = api["coord"]["lon"]
    location_y = api["coord"]["lat"]
    #m = folium.Map(location=[location_x, location_y])
    #m.save("MyMap.html")
    #print(m)
    #weathermaplabel.configure(image=m)


#----------------------------------------------------------------------------------------set Favourites for standart-view on startup
def save_as_favorite():
    """This function saves a Favourite to a json file to have it as Standart startup"""
    filePathName = 'Code/settings/fav.json'
    fav_Name = { "favourite" : city_name.get()}
    with open(filePathName, 'w') as fp:
        json.dump(fav_Name, fp)


#----------------------------------------------------------------------------------------Image
img = ImageTk.PhotoImage(Image.open("Code/settings/Logo_Python.png"))
logo = Label(root, image=img)
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
input_label.grid(row=0, column=1, sticky=W)
inpt.grid(row=0, column=2, sticky=W)
input_button.grid(row=0, column=3, sticky=E)

#----------------------------------------------------------------------------------------weather
city_print = StringVar()
Converter = Button(input_frame, text = "F°", command = celsius_Fahrenheit_converter)
Favourites = Button(input_frame, text = "✰", command = save_as_favorite )
label_date = Label(date_time_frame, font=("Calibri",20), bg="grey",fg="white")
label_clock = Label(date_time_frame, font=("Calibri",20), bg="grey",fg="white")

label_city = Label(weather_frame, textvariable=city_print, font=("bold", 20),bg="light grey")

temp = Label(weather_frame, padx=10, pady=5, font=("bold", 15),bg="light grey")
temp_max = Label(weather_frame, padx=10, pady=0, font=("Calibri", 10),bg="light grey")
temp_min = Label(weather_frame, padx=10, pady=0, font=("Calibri", 10),bg="light grey")
humidity = Label(weather_frame, padx=10, pady=10, font=("Calibri", 10),bg="light grey")
weather_description = Label(weather_frame, padx=10, pady=5, font=("Calibri",15),bg="light blue", borderwidth = 1, relief = "solid")


Converter.grid(row=0, column=4, sticky=E)
Favourites.grid(row=0, column=5, sticky=E)
label_date.grid(row=0, sticky=E)
label_clock.grid(row=1, sticky=E)


label_city.grid(row=0, column=0, sticky=W)
temp.grid(row=2, column=0, sticky=W)
temp_max.grid(row=3, column=0, sticky=W)
temp_min.grid(row=4, column=0, sticky=W)
humidity.grid(row=5, column=0, sticky=W)
weather_description.grid(row=6, column=0, sticky=W, padx=20, pady=20)


#----------------------------------------------------------------------------------------7 Day Forecast
label_eight_day_forecast = Label(eight_day_forecast_frame, text="8-day forecast",font=("bold", 18))
label_day_one = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_two = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_three = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_four = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_five = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_six = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_seven = Label(eight_day_forecast_frame, font=("Calibri", 14))
label_day_eight = Label(eight_day_forecast_frame, font=("Calibri", 14))

label_eight_day_forecast.grid(row=0, column=0, sticky=W)
label_day_one.grid(row=1, column=0, sticky=W)
label_day_two.grid(row=2, column=0, sticky=W)
label_day_three.grid(row=3, column=0, sticky=W)
label_day_four.grid(row=4, column=0, sticky=W)
label_day_five.grid(row=5, column=0, sticky=W)
label_day_six.grid(row=6, column=0, sticky=W)
label_day_seven.grid(row=7, column=0, sticky=W)
label_day_eight.grid(row=8, column=0, sticky=W)

#----------------------------------------------------------------------------------------Weather Map
#weathermaplabel = Label(weathermap_frame)
#weathermap = Button(weathermap_frame, text="test", command = weather_map)



#weathermaplabel.grid(row=0, column=1)
#weathermap.grid(row=1, column=1)



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

