




import numpy as np
import matplotlib.pyplot as plt

# Example historical temperature data (in Celsius)
years = np.array([2000, 2010, 2020])
temperatures = np.array([20.0, 21.5, 22.8])

# Linear regression to estimate temperature trend
coefficients = np.polyfit(years, temperatures, 1)
trend_slope, trend_intercept = coefficients

# Projecting temperatures for future years
future_years = np.array([2030, 2040, 2050])
projected_temperatures = trend_slope * future_years + trend_intercept

# Plotting historical and projected temperatures
plt.figure(figsize=(12, 8))
plt.plot(years, temperatures, 'o', label='Historical Data')
plt.plot(future_years, projected_temperatures, 'x', label='Projected Data')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Climate Change Heat Scenarios')
plt.legend()
plt.grid(True)



import pandas as pd
import matplotlib.pyplot as plt

# Load the temperature data from CSV
data = pd.read_csv('temperature_data.csv') # Date Time,T (degC)

# Assuming the dataset has 'Date' and 'Temperature' columns
data['Date Time'] = pd.to_datetime(data['Date Time'])

# Set a threshold for heat wave definition (e.g., temperature above 30°C)
heat_wave_threshold = 30

# Identify heat wave periods
heat_wave_periods = []
current_heat_wave_start = None 

for index, row in data.iterrows():
    if row['T (degC)'] > heat_wave_threshold:
        if current_heat_wave_start is None:
            current_heat_wave_start = row['Date Time'] 
    else:
        if current_heat_wave_start is not None:
            heat_wave_periods.append((current_heat_wave_start, row['Date Time']))
            print(row['T (degC)'],'???????????????')
            
            current_heat_wave_start = None

# Plotting the temperature data and identified heat waves
plt.figure(figsize=(10, 6))
plt.plot(data['Date Time'], data['T (degC)'], label='T (degC)')
print(heat_wave_periods,'>>>>>>>>>>>>')

Heat_Wave_Duration_ = []
for start, end in heat_wave_periods:
    Heat_Wave_Duration_.append( (end - start).seconds/60./60.)
    plt.axvspan(start, end, color='red', alpha=0.3, label='Heat Wave')
plt.xlabel('Date Time')
plt.ylabel('Temperature (°C)')
plt.title('Climate Change Heat Waves')
plt.legend()
plt.grid(True)

# Plotting the temperature data and identified heat waves
plt.figure(figsize=(10, 6))
Heat_Wave_Number_ = range(len(Heat_Wave_Duration_))
plt.bar(Heat_Wave_Number_,Heat_Wave_Duration_, label='Duration [hours]')
plt.xlabel('# Wave Number')
plt.ylabel('Duration [hours]')
plt.title('Climate Change Heat Waves')
plt.legend()
plt.grid(True)

https://www.kaggle.com/code/wolfy73/co2-evolution
 
 
plt.show()



 
