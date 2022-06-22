import requests.py

API_KEY =  "716c94c9aaf725b99784dd5c16ac8e83"
BASE_URL = "https://home.openweathermap.org/api_keys"

city = input("Enter a city name:  ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temprature = round(data["main"]["temp"] - 273.15, 2)

print("weather:", weather)
print("Temprature:", temprature, "celsius")
else:
print("An error ocurred.")
    