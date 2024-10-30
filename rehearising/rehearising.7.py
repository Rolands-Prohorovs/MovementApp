# import json 
# import pandas as pd
# import matplotlib.pyplot as plt
# import requests


# cpu_data = []
# url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=5&timezone=Europe/Helsinki"
# response = requests.get(url)
# data = response.json()


# for entry in data["feeds"]:
#     movement_value = entry["field1"]
#     temp_value = entry["field2"]
#     time_value = entry["created_at"]
    
  
#     cpu = {
#         'movement': movement_value,
#         'temperature_celsius': float(temp_value),
#         'time': time_value
#     }
    
#     date = cpu['time'][0: 10]
#     clock = cpu['time'][11: 19]
#     date = list(date)
#     date[4] = '/'
#     date[7] = '/'
#     cpu['time'] = ''.join(date)
#     cpu['time'] = clock
#     cpu_data.append(cpu)
# with open("cpu.json", "w") as file:
#     json.dump(cpu_data, file, indent=4)
#     print ("Updated data written to cpu.json")

# df = pd.DataFrame(cpu_data)
# print("Pandas DataFrame:")
# print(df)

# cpu_data.append(cpu)

# df = pd.DataFrame(cpu_data)

# # for i in df['temperature_celsius']:
# #     if i >= 48.8:
# #         print('red')
# #         bar_color = 'red'
# #     else:
# #         print('blue')
# #         bar_color = 'blue'

# #     plt.bar(x =df['time'], height=df['temperature_celsius'], color = bar_color)
# # plt.show()
# # ZZZ
# # df = pd.DataFrame(cpu_data)
# # plt.figure(figsize=(10, 5))
# # plt.plot(df['movement'], label='movement')
# # plt.xlabel('Time')
# # plt.ylabel('Values')
# # plt.title('Movement Over Time')
# # plt.legend()
# # plt.show()



import json
import pandas as pd
import matplotlib.pyplot as plt
import requests

cpu_data = []
url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=5&timezone=Europe/Helsinki"
response = requests.get(url)
data = response.json()

for entry in data["feeds"]:
    movement_value = entry["field1"]
    temp_value = entry["field2"]
    time_value = entry["created_at"]
    
    cpu = {
        'movement': movement_value,
        'temperature_celsius': float(temp_value),
        'time': time_value[:10] + " " + time_value[11:19]
    }
    cpu_data.append(cpu)

with open("cpu.json", "w") as file:
    json.dump(cpu_data, file, indent=4)
    print("Updated data written to cpu.json")

df = pd.DataFrame(cpu_data)
print("Pandas DataFrame:")
print(df)

# Set colors based on temperature condition
if temp >= 48.8:
    colors = 'red'
else:
    colors = 'blue'
colors = ['red' if temp >= 48.8 else 'blue' for temp in df['temperature_celsius']]

# Plot bar chart
plt.figure(figsize=(10, 5))
plt.bar(x=df['time'], height=df['temperature_celsius'], color=colors)
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.show()


