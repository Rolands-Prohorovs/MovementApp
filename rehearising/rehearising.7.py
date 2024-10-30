# import pandas as pd
# import requests
# import json 

# 
# cpu_data = []
# url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20&timezone=Europe/Helsinki"
# response = requests.get(url)
# data = response.json()

# 
# for entry in data["feeds"]:
#     movement_value = entry["field1"]
#     temp_value = entry["field2"]
    
    
#     
#     cpu = {
#         'movement': movement_value,
#         'temperature_celsius': float(temp_value),
#     }
    
#     
#     cpu_data.append(cpu)
# with open("cpu.json", "w") as file:
#     json.dump(cpu_data, file, indent=4)
#     print ("Updated data written to cpu.json")
# 
# df = pd.DataFrame(cpu_data)
# print("Pandas DataFrame:")
# print(df)


import pandas as pd
import matplotlib.pyplot as plt
import requests

cpu_data = []
url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20&timezone=Europe/Helsinki"
response = requests.get(url)
data = response.json()


for entry in data["feeds"]:
    movement_value = entry["field1"]
    temp_value = entry["field2"]
    
    
  
    cpu = {
        'movement': movement_value,
        'temperature_celsius': float(temp_value),
    }
    
    
    cpu_data.append(cpu)

df = pd.DataFrame(cpu_data)

plt.figure(figsize=(10, 5))
plt.plot(df['temperature_celsius'], label='temperature_celsius')
plt.plot(df['movement'], label='movement')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Temperature and Movement Over Time')
plt.legend()
plt.show()