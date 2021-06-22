import requests
from datetime import datetime

print("☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁")
print("🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞WEATHER REPORT🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞🌞")
print("☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁☁")
api_key = 'deb66bf8b78783ede5efaa14cd8dad73'
location = input("Enter the city name: ")
try:
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    temperature_city = ((api_data['main']['temp']) - 273.15)
    weather = api_data['weather'][0]['description']
    hum_dity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
except KeyError:
    print("Invalid city")
with open("weather_report.txt", "w") as data:
    try:
        data.write("\n<==============================================================>")
        data.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
        data.write("\n<==============================================================>")

        data.write("\nCurrent temperature is: {:.2f} deg C".format(temperature_city))
        data.write("\nCurrent weather desc  :" + weather)
        data.write("\nCurrent Humidity      :" + str(hum_dity) + '%')
        data.write("\nCurrent wind speed    :" + str(wind_speed) + 'kmph')
        print("\nThe  weather report of the city " + location + " is stored in weather_report.txt in your current working  directory")
        choice = input("\nDo you want to read  the report (y/n)")
    except NameError:
        exit()
if choice == "y":
    with open("weather_report.txt", "r") as display:
        h = display.read()
        print(h)
else:
    exit()
