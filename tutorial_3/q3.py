"""
@author: Vinay
Question: Find the temperature of the hottest month for each year. (This dataset contains average monthly temp from 1901-2017).
Dataset: NWH_temp_data_25_1901_2017_cru_data
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')
per_year_temperature = np.array([])
max_temperature = np.array([])
years = np.array([])
count = 0
for column in df:
    year = 1900
    for row in df[column]:
        count += 1
        per_year_temperature = np.append(per_year_temperature, row)
        if count == 12:
            year += 1
            years = np.append(years, year)
            max_temperature = np.append(max_temperature, np.amax(per_year_temperature))
            per_year_temperature = np.array([])
            count = 0
    
    plt.plot(years, max_temperature)
    max_temperature = np.array([])
    years = np.array([])
    plt.title('Temperature of the hottest month')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.xlabel('Years')
    plt.ylabel('Temperature')