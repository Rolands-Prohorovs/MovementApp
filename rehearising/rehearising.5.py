
# PossibleHTTP requests are:
# GET
# POST
# PUT- update, replace the old resource with a new one
# PATCH - update, pertial modifications to a resource
# DELETE
# import requests

# url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20" # important to hide the api key so no one can delete your info!!!!!!!!!!!
# response = requests.get(url)
# print(f"Status code: {response.status_code}")
# data = response.json()

# for entry in data["feeds"]:
#     movement_value = entry["field1"]
#     temp_value = entry["field2"]
#     time_value = entry["created_at"]
#     print(f"Movement value: {movement_value}")
#     print(f"Temperature value: {temp_value}")
#     print(f"At: {time_value}")




# Getting train schedule
# import requests


# # Base URL for the VR API
# base_url = "https://rata.digitraffic.fi/api/v1/live-trains/station"


# # Departure and arrival station short codes
# if input('Do you wanna go from Helsinki->Lahti or Lahti->Helsinki: ') != 'Lahti->Helsinki: ':
#     departure_station = "HKI" # Helsinki
#     arrival_station = "LH" # Lahti
# else:
#     departure_station = "LH" # Lahti
#     arrival_station = "HKI" # Helsinki

# # Complete URL
# url = f"{base_url}/{departure_station}/{arrival_station}"


# # Make a GET request to the API
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:

#     # Parse the JSON response
#     trains = response.json()

#     for train in trains:
#         train_number = train["trainNumber"]
#         # Initialize variables to store departure and arrival times

#         scheduled_departure = None
#         actual_departure = None
#         scheduled_arrival = None
#         actual_arrival = None

#         # Find the departure and arrival times from the timetable rows
#         for row in train["timeTableRows"]:
#             if row["stationShortCode"] == departure_station and row["type"] == "DEPARTURE":
#                 scheduled_departure = row["scheduledTime"]
#             if row["stationShortCode"] == arrival_station and row["type"] == "ARRIVAL":
#                 scheduled_arrival = row["scheduledTime"]

#         print(f"Train Number: {train_number}, "
#             f"Departure: {scheduled_departure}, "
#             f"Arrival: {scheduled_arrival}")
# else:
#     print(f"Failed to retrieve train data. Status code: {response.status_code}")

# Data to be written to the text file
data = """Hello, World!
This is a simple text file.
It contains multiple lines of text."""

# Writing to the text file
with open("data.txt", "w") as file:
    file.write(data)
    
print("Data written to data.txt")