import requests

SHEETY_API_ENDPOINT = ""
SHEETY_API_USERS_EP = ""
AUTH = ""

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {
            "Authorization": AUTH
        }
        response = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        headers = {
            "Authorization": AUTH
        }
        customers_endpoint = SHEETY_API_USERS_EP
        response = requests.get(url=customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
