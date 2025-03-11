import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID_SHEETY")
API_KEY = os.environ.get("API_KEY_SHEETY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
AUTH_SHEETY = os.environ.get("AUTH_SHEETY")


WEIGHT_KG = "number format"
HEIGHT_CM = ""
AGE = ""

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": text,
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)
data = response.json()

#making a post request to sheety
sheety_endpoint = SHEETY_ENDPOINT

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.time().__str__()[:8]
#or time_now = now.strftime("%X")


for exercise in data["exercises"]:
    workout_info = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        },
    }

    #making authentication in our sheety
    header = {
        "Authorization": AUTH_SHEETY
    }

    res = requests.post(url=sheety_endpoint, json=workout_info, headers=header)
    print(res.json())



