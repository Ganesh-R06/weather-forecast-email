import requests
import pandas as pd
from smtplib import *
my_email="kdark8276@gmail.com"
passkey="hzdo btpg wxux kbpv"

my_api="f989549b9517f6a418526b372d963348"
params = {
    "lat": 49.655338,
    "lon": 13.290880,
    "appid": my_api,
    "units": "metric",
    "cnt":4
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=params
)

response.raise_for_status()
weather_data = response.json()
# weather_id=weather_data["list"][0]["weather"][0]["id"]
will=False
for hour in weather_data["list"]:
    condition=hour["weather"][0]["id"]
    if int(condition)<=700:
       will=True
if will:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passkey)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ganesh20066@yahoo.com",
                            msg="Subject: Weather forecast \n\n Bring Umbrella")
else:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passkey)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ganesh20066@yahoo.com",
                            msg="Subject:Weather forecast \n\n Don't bring Umbrella")

print("email sent successfully")