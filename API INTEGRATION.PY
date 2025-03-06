import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta

# Replace with your own API key
api_key = '0bf86e774e587c4cf21cf82831873379'
city = 'BHUBANESWAR'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Parse the data
dates = []
temperatures = []
# Ensure we are referencing the correct part of the response
for entry in data['list']:
    dates.append(datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S'))
    temperatures.append(entry['main']['temp'])

# Create a DataFrame
weather_data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperatures
})

# Plotting the data
plt.figure(figsize=(10, 5))
sns.barplot(data=weather_data, x='Date', y='Temperature')
plt.title(f'Temperature Forecast for {city}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# colour implement in chart



# Show the plot
plt.show()
