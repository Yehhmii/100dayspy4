import requests
from datetime import datetime
import os

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

## creating a user in pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

##possting a pixel to the graph
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commit coding have you done today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)


##using PUT request to update a post
update_endpoint = f"{pixel_endpoint}/20240109"

update_keys = {
    "quantity": "7"
}

# response = requests.put(url=update_endpoint, json=update_keys, headers=headers)
# print(response.text)

##using Delete on our graph
delete_endpoint = f"{pixel_endpoint}/20240108"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
