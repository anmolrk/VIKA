from tkinter import *
from tkinter import messagebox
import requests


url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

api_key = 'bcf589bf3a118b08bb2e67c66a87ccd7'

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()

        country = json['sys']['country']

        temp_kelvin = json['main']['temp']
        temp_celcius = temp_kelvin - 273.15 
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32


        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']

        final =  (city, country, temp_celcius, temp_fahrenheit, icon, weather)

        return final
        
        # print(country)
        # print(temp_kelvin)
        # print(icon)
        # print(weather)   
    else:
        return None

# print(get_weather('London'))

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        print(weather)
        location_lbl['text'] = f'{weather[0]}, {weather[1]}' 
        img_weather['file'] = f'weatherIcon/{weather[4]}.png'
        temp_lbl['text'] = f'{int(weather[2])}°C, {int(weather[3])}°F'
        weather_lbl['text'] = weather[5]

    else:
        messagebox.showerror('Not Found', f'Cannot find city {city}')
    
    city_entry.delete(0, END)



app = Tk()
app.title("Weather Powered by V.I.K.A.")
app.geometry("350x350")


f_app=Frame(app, bg='white')
f_app.pack(fill="both",expand="yes")

city_text = StringVar()
city_entry = Entry(f_app, textvariable=city_text,bg="#e6e6e6",width=32,font=("Verdana"))
city_entry.pack(pady=20)



search_btn = Button(f_app,text="Searech Weather", width=15, command=search,relief=GROOVE, height=1)
search_btn.pack()

wrapper=LabelFrame(f_app, text="Weather Powered by OpenWeatherMap.ORG", bg='white')
wrapper.pack(pady=10, padx=10 ,fill="both",expand="yes")

location_lbl = Label(wrapper, text='', font=('bold',20),bg='white')
location_lbl.pack(pady=5)

img_weather = PhotoImage(file='')
image = Label(wrapper, image=img_weather,bg='white')
image.pack()

temp_lbl = Label(wrapper, text='',bg='white')
temp_lbl.pack()

weather_lbl = Label(wrapper, text='',font=('bold',18),bg='white')
weather_lbl.pack()

def enter_function(event):
    search_btn.invoke()
    
app.bind('<Return>', enter_function)

app.mainloop()