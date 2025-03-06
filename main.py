from client import APIClient
from endpoints import APIEndpoints
from time import sleep

# Initialize the client
client = APIClient(base_url="https://192.168.10.61", auth_token="your_auth_token")

api = APIEndpoints(client)

response = api.login(username="5AHIT", password="5ahiT")
token = response[0]["result"]["token"]
client.set_auth_token(token)

print(api.write_speed("\"Motor\".Sollgeschwindigkeit", 1000))

sleep(3)
print(api.write_speed("\"Motor\".Sollgeschwindigkeit", 0))

