"""
file: Wind Chill.py
author: Zach Southwick

purpose: Calculate the wind chill based on an initial starting temperature.
"""

def temp_convert(temp):
    celsius = ((temp * 9) / 5) + 32
    return celsius

def wind_chill(temp, wind_speed):
    chill_temp = 35.74 + (.6215 * temp) - (35.75 * (wind_speed ** .16)) + (.4275 * temp * (wind_speed ** .16))
    return chill_temp

temp = float(input('What is the temperature? '))
system = input('Farenheit or Celsius (F/C)? ')
if system.lower() == 'c':
    temp = temp_convert(temp)
for i in range(5, 61, 5):
    new_temp = wind_chill(temp, i)
    print(f'At temparature {temp:.1f}, and wind speed {i} mph, the windchill is: {new_temp:.2f}F')