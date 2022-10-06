"""
@author: Vinay
Question: Store the hottest temperature of the month (which is calculated in the above question) in a data frame and export it to your working directory).
Dataset: NWH_temp_data_25_1901_2017_cru_data
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')
max_temperature = pd.DataFrame(columns = ["years"])
for dummy in range(1901, 2018):
    max_temperature = max_temperature.append({'years': dummy}, ignore_index=True)

max_temperature[df.columns] = np.nan
per_year_temperature = np.array([])
count = 0
for column in df:
    year = 1900

    for row in df[column]:
        count += 1
        per_year_temperature = np.append(per_year_temperature, row)
        if count == 12:
            year += 1
            max_temperature.loc[max_temperature.years == year, column] = np.amax(per_year_temperature)
            per_year_temperature = np.array([])
            count = 0
max_temperature.to_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_3\hottest_temperature_years.csv', index = False)