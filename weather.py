import os

from twilio.rest import Client
import requests

account_sid = "AC4d0f9055c60156aa6ba46220c9e063c7"
auth_token = "de3400cc07dc751cc8f2fe37c908e1e6"
Api_key2 = os.environ.get("api_key")
#"c90c660f904f07fd7b7f71b6ce617dbf"
Api_key = "e6bea81db52b67f0aca59d78954b40b9"

#response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Essen,DE&appid={Api_key}")
response = requests.get(f"https://api.openweathermap.org/data/2.8/onecall?lat=51.759050&lon=19.458600&appid={Api_key2}")
response.raise_for_status()
weather_data = response.json()["hourly"]
print(weather_data)
#for items in weather_data[0:12]:
    #print(items)
will_rain = False
weather_forecast = []
for item in weather_data[0:12]:
    for k,v in item.items():
        if k == "weather":
            for x in v:
                weather_forecast.append(x)
                for a in weather_forecast:
                    if a["id"] < 700:
                        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Remember to take an ⛱️",
                         from_="+16076954991",
                         to="+4917661259157"
                     )

    print(message.status)

"""for things in  weather_forecast:
    for k,v in things.items():
        if k == "description" and v == "scattered clouds":
            print(k)"""