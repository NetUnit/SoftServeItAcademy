from tkinter import *
from configparser import ConfigParser
import requests
import tkinter as tk
import PIL
from PIL import Image, ImageTk

import pyowm.owm
from pyowm.owm import OWM

owm = OWM('8387b7e23ef87eb351bc3497d07a6dbc')

#url = 'https://api.openweathermap.org/data/2.5/weather'

api_key = '8387b7e23ef87eb351bc3497d07a6dbc'

# 1 GET A CURRENT WEATHER STATUS OF THE CITY


def get_weather(city):  # main class

    try:
        # owm block
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        w = observation.weather

        # get_short_weather_status
        # short version of status (eg. 'Rain')
        sh_status = w.status
        # detailed version of status (eg. 'light rain')
        det_status = w.detailed_status

        # get_id_city
        registry = owm.city_id_registry()
        id_result = registry.ids_for(city)[0]

        # get_weather_options
        wi = w.wind()['speed']
        hu = w.humidity
        tmax = w.temperature('celsius')['temp_max']
        tmin = w.temperature('celsius')['temp_min']
        t_feel = w.temperature('celsius')['feels_like']

        # get_pressure
        # in pyOWM ---weather--- is an inbuilt method
        pressure_dict = observation.weather.pressure
        # press (atmospheric pressure on the ground in hPa)
        pressure1 = pressure_dict['press']
        pressure2 = pressure_dict['sea_level']

        # get coords
        list_of_locations = registry.locations_for(city)
        # list of locatins - dictionary # will get allways 1'st by default
        location = list_of_locations[0]
        lat = round((location.lat), 2)
        lon = round((location.lon), 2)

        # get sunrise & sunset
        # it's 10800 seconds = 3 hours # default unit: 'unix'
        sunrise_unix = w.sunrise_time() + 10800
        sunrise_local = (pyowm.utils.formatting.timeformat(
            sunrise_unix, 'iso'))[10:-3]

        sunset_unix = w.sunset_time() + 10800  # default unit: 'unix'
        sunset_local = (pyowm.utils.formatting.timeformat(
            sunset_unix, 'iso'))[10:-3]

        # get rain for the last 1-12 hours (depends on meteo json response)
        rain_dict = observation.weather.rain

        final = (wi, hu, tmax, tmin, t_feel, pressure1, pressure2, id_result, lat, lon, sunrise_local, sunset_local, rain_dict,
                 sh_status, det_status)                     											# <Weather - reference time=2013-12-18 09:20, status=Clouds>
        return (final)

    except:
        final = 'Oops, something went wrong!'


# functionality of the app
def get_short_status():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = (
            f'Weather status: {weather[13]}. Precipitation: {weather[14]} ')
    else:
        error_lbl['text'] = (
            f'We could\'nt start your program. Please try starting it again')


def get_id_city():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = (f'City ID: {weather[7]}')
    else:
        error_lbl['text'] = (
            f'We couldn\'t start your program. Please try starting it again')


def get_weather_options():
    city = city_text.get()
    weather = get_weather(city)

    if weather:
        location_lbl['text'] = (f'Clouds: {weather[13]}')
        temp_lbl['text'] = (
            f'Tmax {weather[2]} °C |  Tmin {weather[4]} °C | feels-like T {weather[3]} °C')
        weather_lbl['text'] = (
            f'Wind: {weather[0]} m∕s | Humidity {weather[1]} %')
    else:
        error_lbl['text'] = (
            f'We could\'nt start your program. Please try starting it again')


def get_pressure():
    city = city_text.get()
    pressure = get_weather(city)

    if pressure:
        location_lbl['text'] = (f'{pressure[5]} bar∕mPa∕atm ')
    else:
        error_lbl['text'] = (
            f'We could\'nt start your program. Please try starting it again')


def get_coords():
    city = city_text.get()
    coords = get_weather(city)

    if coords:
        location_lbl['text'] = (f'Lat: {coords[8]} Lon: {coords[9]}')
    else:
        error_lbl['text'] = (
            f'We could\'nt start your program. Please try starting it again')


def get_sunrise():
    city = city_text.get()
    sunrise = get_weather(city)

    if sunrise:
        location_lbl['text'] = (
            f'Sunrise time: {sunrise[10]}s Sunset time: {sunrise[11]}s')
    else:
        error_lbl['text'] = (
            f'We could\'nt start your program. Please try starting it again')


def get_rain():
    city = city_text.get()
    rain = get_weather(city)
    try:
        if rain:
            rr = rain[12]['1h']
            #location_lbl['text'] = (f'{rr}')
            location_lbl['text'] = (
                f'Last {str(rr)[2:3]} hour: {str(rr)[-5:-1]}mm')
        else:
            error_lbl['text'] = (
                f'We could\'nt start your program. Please try starting it again')

    except KeyError:
        error_lbl['text'] = (
            f'Ooops. There is no sufficient amount of rain to determine:')

# one_call data (forecast for the next day)


def get_one_call():
    try:
        city = tom_forecast_city.get()
        forecast = get_weather(city)

        mgr = owm.weather_manager()
        registry = owm.city_id_registry()
        list_of_locations = registry.locations_for(city)

        # list of locatins - dictionary # will get allways 1'st by default
        location = list_of_locations[0]
        lat = round((location.lat), 2)
        lon = round((location.lon), 2)

        one_call = mgr.one_call(lat, lon)

        tom_temp = one_call.forecast_daily[0].temperature(
            'celsius').get('feels_like_morn', None)
        tom_wi = one_call.forecast_hourly[12].wind().get('speed', 0)
        tom_hu = one_call.forecast_hourly[12].humidity

        if forecast:
            location2_lbl['text'] = (f'Feels like morning T: {tom_temp}°C.\n\
            Wind: {tom_wi} m∕s. \n\
            Humidity: {tom_hu} %')
        else:
            error_lbl['text'] = (
                f'There may be not enough info now. Please try again later')
    except:
        location2_lbl['text'] = (f'We could\'nt start your program. \n\
         Please try starting it again')


##############################################################################################
# tkinter GUI

app = Tk()  # create a an app Variable

app.title('WEATHER APP')

app.geometry('525x650')  # 1000 width 400 height

###############################################################################################

# search window#1 parameters # це меню вводу параметрів

space2_lbl = Label(app, text='', font=('bold', 15), height=4)
space2_lbl.pack()

# search window#1 parameters # це меню вводу параметрів

city_text = StringVar()
city_entry = Entry(app, justify=CENTER, width=43, textvariable=city_text)
# pack function - place a button on the screen (pack() is a placing function)
city_entry.pack()

###############################################################################################

# Info status depending on the city
location_lbl = Label(app, text='Location', font=('bold', 15), bg='#afb2b7')
location_lbl.pack()

# button#1 get_id
search_btn = Button(app, text='Check ID', width=40,
                    bg='#f95a19', command=get_id_city)
search_btn.pack()

# button#2 get_short_status
search_btn7 = Button(app, text='Short Weather Status',
                     bg='#f95a19', width=40, command=get_short_status)
search_btn7.pack()

# button#3 get_weather_options
search_btn2 = Button(app, text='Detailed Weather Status',
                     bg='#f95a19', width=40, command=get_weather_options)
search_btn2.pack()

# button#4 get_pressure
search_btn3 = Button(app, text='Check Pressure', width=40,
                     bg='#f95a19', command=get_pressure)
search_btn3.pack()

# button#5 get_coords
search_btn4 = Button(app, text='Check Coords', width=40,
                     bg='#f95a19', command=get_coords)
search_btn4.pack()

# button#6 get_sunrise_
search_btn5 = Button(app, text='Check Sunrise∕Sunset Time',
                     bg='#f95a19', width=40, command=get_sunrise)
search_btn5.pack()

# button#7 get_rain
search_btn6 = Button(app, text='Check Rain Amount',
                     bg='#f95a19', width=40, command=get_rain)
search_btn6.pack()

# Program status
error_lbl = Label(app, text='Program Status: OK', font=('bold', 10))
error_lbl.pack()

# Picture status
image = Label(app, bitmap='')
image.pack()

# temperature status
temp_lbl = Label(app, text='temperature')
temp_lbl.pack()

# weather status
weather_lbl = Label(app, text='weather')
weather_lbl.pack()

# blanks space between buttons
space_lbl = Label(app, text='', font=('bold, 20'))
space_lbl.pack()

# tomorrows weather
tom_forecast_city = StringVar()
forecast_entry = Entry(app, width=43, textvariable=tom_forecast_city)
forecast_entry.pack()  # tomorrow mornings weather

# forecast string
location2_lbl = Label(app, text='Location', font=('bold', 15), bg='#afb2b7')
location2_lbl.pack()

# tomorrow's forecast string
# button#8 forecast_for_tomorrow
forecast_btn = Button(app, text='Tomorrow Forecast',
                      bg='#f95a19', width=40, command=get_one_call)
forecast_btn.pack()

###############################################################################################
## icon (clouds+sun)

#app = Tk()
# root.geometry("550x300+300+150")
#app.resizable(width=True, height=True)

img = Image.open(
    "/media/netunit/SSD.LI/PythonCore/Project_LV-527/weather_app/images/11n@2x.png")
photo = ImageTk.PhotoImage(img)
#img = img.resize(100, 100, '11n@2x.png')
lab_img = Label(image=photo).place(x=0, y=0)

###############################################################################################
# icon in the menue - should be corrected
#app.iconbitmap('/home/netunit/Стільниця/Soft/Project LV-527/myproject/images∕Cloudy_Rain.ico')

#app = tk.Tk()
#app.tk.call('wm', 'iconphoto', app._w, tk.PhotoImage(file='/home/netunit/Стільниця/Soft/Project LV-527/myproject/venv∕tmp.png'))

# app = tk.Tk()

# app.iconphoto(False, tk.PhotoImage(file='/home/netunit/Стільниця/Soft/Project LV-527/myproject/venv∕tmp.png'))
# app.mainloop()

app.mainloop()  # function to create the main window
