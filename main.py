import requests
from smtplib import *
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("EMAIL")
passkey = os.getenv("PASSWORD")
my_api = os.getenv("OPENWEATHER_API_KEY")
to_addr = os.getenv("TO_EMAIL")
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
                            to_addrs=to_addr,
                            msg="Subject: Weather forecast \n\n Bring Umbrella")
else:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passkey)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_addr,
                            msg="Subject:Weather forecast \n\n Don't bring Umbrella")

print("email sent successfully")
