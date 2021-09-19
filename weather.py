from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
import json
import time

root = Tk()
root.title("RainCloud")
root.iconbitmap("images\Weather.ico")
root.geometry("750x500")
root['background'] = "white"


# title
title= Label(root, text="\nCurrent Weather", font= ("arial", 12, "bold"), fg='white', bg='black', anchor=NW, padx=10, pady=5)
title.place(x=0,y=0, relwidth=1, height=90)

# pannel 
location= Entry(root, font=("arial", 13), width=77, fg='black', bg='#f0bf43', bd=0)
location.place(x=10,y=50,height=30)

#function
def popup():
    messagebox.showerror("Not Found", "Invalid City.\n Please enter valid city")

def getweather():
    loca = location.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+loca+"&appid=3e0cd0cfdf7135a53bf72064bdad403f"
    api_request = requests.get(api)
    data = json.loads(api_request.content)
    id = data['cod']

    if id == "404":
        popup()
        
    else:

        condition = data['weather'][0]['main']
        y = data['main']
        temp = int(y['temp']-273.15)
        max_temp = int(y['temp_max']-273.15)
        min_temp = int(y['temp_min']-273.15)
        pressure = y['pressure']
        humidity = y['humidity']
        wind = int(data['wind']['speed'] * 3.6)
        x = data['sys']
        country = x['country']
        timezone = data['timezone']
    
        sunrise = time.strftime("%I:%M:%S", time.gmtime(x['sunrise'] + timezone))
        sunset = time.strftime("%I:%M:%S", time.gmtime(x['sunset'] + timezone))
        name = data['name']
        

        # #adding the recieved info to screen
        label_city.configure(text=name + ", " + country, bg="#d0d5db")
        label_temp.configure(text=str(temp)+"°C")
        label_condition.configure(text=condition)
        label_humidity.configure(text="Humidity: "+str(humidity)+" %")
        label_wind.configure(text="Wind: "+str(wind)+" km/h")
        label_pressure.configure(text="Pressure: "+str(pressure)+ "mb")


        label_min_temp.configure(text="Min Temp: "+ str(min_temp)+ "°C")
        label_max_temp.configure(text="Max Temp: "+ str(max_temp)+ "°C")

        label_sunrise.configure(text="Sunrise: "+ str(sunrise) + " AM")
        label_sunset.configure(text="Sunset: "+ str(sunset) + " PM")

        #images
        thermo_label.configure(image=thermo) 
        sun_label.configure(image=sun) 

# search button
search_icon = Image.open("images\search.png")
search_icon = search_icon.resize((30, 30), Image.ANTIALIAS)
search_icon = ImageTk.PhotoImage(search_icon)

search = Button(root, image=search_icon, bd=0, bg="black", activebackground="#fcba03", command = getweather)
search.place(x=700, y=50,height=30)

f=("arial", 15, "bold")

label_city = Label(root, text="", font=("arial", 25, "bold"), bg="white")
label_city.pack(fill="both")
label_city.place(x=20, y=110)

label_temp = Label(root, font=("arial", 45, "bold"), bg="white")
label_temp.place(x=100, y=180)

label_condition = Label(root, font=("arial", 20, "bold"),fg="#0f0361", bg="white")
label_condition.place(x=70, y=260)

label_humidity = Label(root, font=f,bg="white")
label_humidity.place(x=20, y=340)

label_wind = Label(root, font=f, bg="white")
label_wind.place(x=20, y=370)

label_pressure = Label(root, font=f, bg="white")
label_pressure.place(x=20, y=400)

label_max_temp = Label(root, font=f, bg="white")
label_max_temp.place(x=450, y=230)

label_min_temp = Label(root, font=f, bg="white")
label_min_temp.place(x=450, y=260)

label_sunrise = Label(root, font=f, bg="white")
label_sunrise.place(x=450, y=350)

label_sunset = Label(root, font=f, bg="white")
label_sunset.place(x=450, y=380)

#image
thermo = Image.open("images//thermo.jpg")
thermo = thermo.resize((100, 100), Image.ANTIALIAS)
thermo = ImageTk.PhotoImage(thermo)
thermo_label = Label(root, bd=0, bg="white")
thermo_label.place(x=350, y=200)

sun = Image.open("images\sun.png")
sun = sun.resize((100, 100), Image.ANTIALIAS)
sun = ImageTk.PhotoImage(sun)
sun_label = Label(root, bd=0, bg="white")
sun_label.place(x=350, y=330)

root.mainloop()