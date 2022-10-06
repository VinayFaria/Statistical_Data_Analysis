"""
@author: vinay
"""

import pandas as pd

df = pd.read_excel(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\annual_max_rainfall_1901_2014_cru_india_1x1.xlsx')

Telangana_dataframe = df[["X80.518.5"]]
mean_rainfall_Telangana = Telangana_dataframe["X80.518.5"].mean()
Telangana_years = []
print("Average rainfall of Telangana:", mean_rainfall_Telangana, "mm")
count1 = 0
for ind in Telangana_dataframe.index:
    dummy1 = Telangana_dataframe['X80.518.5'][ind]
    if dummy1 < mean_rainfall_Telangana:
        Telangana_years.append(df['year'][ind])
        count1 += 1

Chattisgarh_dataframe = df[["X82.522.5"]]
mean_rainfall_Chattisgarh = Chattisgarh_dataframe["X82.522.5"].mean()
print("Average rainfall of Chattisgarh:", mean_rainfall_Chattisgarh, "mm")
count2 = 0
for ind in Chattisgarh_dataframe.index:
    dummy2 = Chattisgarh_dataframe['X82.522.5'][ind]
    if dummy2 < mean_rainfall_Chattisgarh:
        count2 += 1

print("Number of years in which rainfall was above average between years 1901 to 2014 in Telangana: ", count1)
print("Number of years in which rainfall was above average between years 1901 to 2014 in Chattisgarh: ", count2)

