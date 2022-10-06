"""
@author: Vinay
Question: Plot the annual mean temperature of the above dataset. (To plot annual mean temperature, first you need to find the average temp of each year).
Dataset: NWH_temp_data_25_1901_2017_cru_data
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')

average_temp = np.array([])
years = np.array([])
count = 0
per_year_temperature = 0

for column in df:
    year = 1900
    for row in df[column]:
        count += 1
        per_year_temperature += row
        if count == 12:
            year += 1
            years = np.append(years, year)
            average_temp = np.append(average_temp, per_year_temperature/12)
            per_year_temperature = 0
            count = 0

    plt.plot(years, average_temp)
    average_temp = np.array([])
    years = np.array([])
    plt.title('Annual mean temperature')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.xlabel('Years')
    plt.ylabel('Temperature')