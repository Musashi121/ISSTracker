import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss position"]["longitude"]
# latitude = data["iss position"]["latitude"]
#
# iss_position = (longitude, latitude)

parameters = {
    "lat": 51.507351,
    "lng": -0.127758,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
