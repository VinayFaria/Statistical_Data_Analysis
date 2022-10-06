"""
@author: Vinay
Question: Find the range (difference between maximum and minimum value) of monthly temperature for the last ten years. Also, plot it.
Dataset: NWH_temp_data_25_1901_2017_cru_data.csv
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')

per_year_temperature = np.array([])
range_temperature = np.array([])
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
            range_temperature = np.append(range_temperature, np.amax(per_year_temperature)-np.amin(per_year_temperature))
            per_year_temperature = np.array([])
            count = 0

    plt.plot(years[100:117], range_temperature[100:117])
    years = np.array([])
    range_temperature = np.array([])
    plt.title('Last 10 years temperature range variation')
    plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
    plt.xlabel('Years')
    plt.ylabel('Maximum - Minimum of Temperature')