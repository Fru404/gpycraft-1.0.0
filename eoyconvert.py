import re
import json
import pandas as pd

data = """
Humidity: 69.00 %
Temperature: 16.60 °C, Humidity: 69.00 %
Temperature: 16.60 °C, Humidity: 69.00 %
DHT11 Sensor Test
Temperature: 16.60 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.50 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 69.00 %
Temperature: 16.40 °C, Humidity: 70.00 %
Temperature: 16.40 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.30 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
Temperature: 16.20 °C, Humidity: 70.00 %
"""


pattern = re.compile(r'Temperature: (\d+\.\d+) °C, Humidity: (\d+\.\d+) %')


matches = pattern.findall(data)


result = [{'Temperature': float(temp), 'Humidity': float(humidity)} for temp, humidity in matches]


json_data = json.dumps(result, indent=4)

with open("sensor1.json",'w') as wr:
    wr.write(json_data)

data=json.loads(json_data)

df=pd.DataFrame(data)
df.to_excel("sensor1.xlsx", index=False)

df.to_csv("sensor1.csv",index=False)